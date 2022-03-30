from django.contrib import admin
from project_app.models import Product

from project_app.models import Category

from project_app.models import Cart

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)