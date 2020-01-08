from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Signup_Form(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class Login_Form(forms.Form):
    password = forms.PasswordInput()
    email = forms.EmailField()
