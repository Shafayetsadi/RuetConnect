from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # Add email field to the UserCreationForm
    email = forms.EmailField()

    # Meta class gives us a nested namespace for configurations and keeps the configurations in one place
    class Meta:
        # Model that will be affected
        model = User
        # Fields that will be shown on the form and in what order
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'image']