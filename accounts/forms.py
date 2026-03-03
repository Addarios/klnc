from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # Dodajemy checkbox newslettera
    subscribe_newsletter = forms.BooleanField(
        required=False, 
        initial=True, 
        label="Chcę otrzymywać informacje o nowościach i ofercie!"
    )

    class Meta:
        model = User
        fields = ['username', 'email']