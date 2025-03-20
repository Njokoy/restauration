from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'password1', 'password2']
