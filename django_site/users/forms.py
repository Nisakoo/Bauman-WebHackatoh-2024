from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
