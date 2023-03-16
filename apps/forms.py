from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.models import Users


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = Users
        fields = ('username', 'email')
