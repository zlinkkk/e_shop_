from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, label='Почта', widget=forms.EmailInput())
    password = forms.CharField(max_length=100, label='Пароль', widget=forms.PasswordInput())
