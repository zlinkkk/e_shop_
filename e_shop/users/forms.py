from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User