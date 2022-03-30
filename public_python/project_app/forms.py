from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Login', max_length=50)
    password = forms.CharField(label='Hasło', max_length=50, widget=forms.PasswordInput())
    mail = forms.EmailField(label='Adres e-mail')

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=50)
    password = forms.CharField(label='Hasło', max_length=50, widget=forms.PasswordInput())