from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from .models import Product, Category, Cart
from django.db.models import Q


def homepage(request):
    template_name = 'home.html'
    if request.user.is_authenticated:
        template_name = 'home_logged.html'
    return render(request, template_name)

class EditProfileTemplateView(TemplateView):
    template_name = 'edit_profile.html'

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            mail = request.POST.get('mail', None)
            if User.objects.filter(username = username).first():
                messages.add_message(request, messages.ERROR, 'Login: "%s" - już jest w bazie!' % login)
                return HttpResponseRedirect('/login')
            # for i in users:
            #     if login == i.username:
            #         messages.add_message(request, messages.ERROR, 'Login: "%s" - już jest w bazie!' % login)
            #         return redirect('/register')
            user = User.objects.create_user(username=username, password=password, email=mail)
            user.is_staff = False
            user.save()
            messages.add_message(request, messages.INFO, 'Konto utworzone! - zaloguj się')
            return HttpResponseRedirect('/login')
    return render(request, 'register_form.html', {'form': form})

def log(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            auth = authenticate(username=username, password=password)
            if auth is not None:
                login(request, auth)

                current_user = request.user

                # messages.add_message(request, messages.INFO, 'Zalogowano!')
                return redirect('/')
            else:
                return HttpResponse(f"nie zalogowano")
    return render(request, 'login_form.html', {'form': form})


@login_required
def edit_profile(request):
    password = request.POST.get('password', None)
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    if password is not '':
        request.user.set_password(password)
        request.user.save()
        messages.add_message(request, messages.INFO, 'Zaloguj ponownie!')
        return redirect('/login')
    if first_name or last_name is not '':
        if first_name is not '':
            user = request.user
            user.first_name = first_name
            user.save()
        if last_name is not '':
            user = request.user
            user.last_name = last_name
            user.save()
        messages.add_message(request, messages.INFO, 'Zmiany zapisane!')
        return redirect('/edit_profil')
    messages.add_message(request, messages.INFO, 'Brak zmian!')
    return redirect('/edit_profil')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def add_product_view(request):
    cat = Category.objects.filter()
    context = {'category': cat}
    return render(request, "add_product_form.html", context)

@login_required
def add_product(request):
    prod_name = request.POST.get('product_name', None)
    cat_id = request.POST.get('radiocat', None)

    if prod_name is "":
        messages.error(request, 'Nie podano nazwy produktu!')

    if cat_id is None:
        messages.add_message(request, messages.ERROR, 'Nie wybrano kategorii produktu!')

    if prod_name and cat_id is not None:
        user = request.user
        category = Category.objects.get(id=cat_id)
        prod = Product.objects.filter(Q(user_id = user.id) | Q(user_id = 1))
        for i in prod:
            if str(prod_name.upper()) == str(i.product_name.upper()):
                messages.add_message(request, messages.ERROR, 'Produkt: "%s" - już jest w bazie!' %prod_name)
                return redirect('/add_product_view')

        formated_neme = prod_name.lower().capitalize()
        data = Product(product_name=formated_neme, category=category, user_id=user)
        data.save()
        messages.add_message(request, messages.SUCCESS, 'Produkt został dodany!')
        return redirect('/add_product_view')

    return redirect('/add_product_view')


@login_required
def cart_view(request):
    prod = Cart.objects.order_by('product__category').filter(user=request.user)
    context = {'product': prod}
    return render(request, "cart.html", context)


@login_required
def add_to_cart(request):
    product_id = request.POST.get('product', None)
    user = request.user
    products_in_cart = Cart.objects.filter(user=user)
    product = Product.objects.get(id=product_id)
    for i in products_in_cart:
        if product.id == i.product.id:
            messages.add_message(request, messages.WARNING, 'Produkt jest już w koszyku!')
            return redirect('/my_search')

    data = Cart(product=product, user=user)
    data.save()
    messages.add_message(request, messages.INFO, 'Produkt został dodany do listy!')
    return redirect('/my_search')


@login_required
def my_search(request):
    user = request.user
    search_input = request.POST.get('product_name', '')
    all_products = Product.objects.filter(Q(user_id = user.id) | Q(user_id = 1)).order_by('product_name')
    cat_id = request.POST.get('radiocat', None)
    cat = Category.objects.filter()
    context = {'product': all_products, 'category': cat}
    if search_input is not '':
        context = {}
        for product in all_products:
            if str(search_input.upper()) in product.product_name.upper():
                q_set = Product.objects.filter(product_name = product.product_name).filter(Q(user_id = user.id) | Q(user_id = 1))
                context = {'product': q_set, 'category': cat}

    if search_input is '' and cat_id is not None:
        context = {}
        category = Category.objects.get(id=cat_id)
        filtered_products = Product.objects.filter(category=category).filter(Q(user_id = user.id) | Q(user_id = 1)).order_by('product_name')
        context = {'product': filtered_products, 'category': cat}

    return render(request, "my_search_form.html", context)



@login_required
def delete_from_cart(request):
    product_id = request.POST.get('product', None)
    user = request.user
    product = Product.objects.get(id=product_id)
    data = Cart.objects.filter(product=product, user=user)
    data.delete()
    messages.add_message(request, messages.INFO, 'Produkt został usunięty z listy!')
    return redirect('/cart')

