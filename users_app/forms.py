

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

# User = get_user_model()

from users_app.models import NewUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ("email",'full_name' , 'phone' , )
        exclude = ('Role',)
        # field_classes = {'email': UsernameField}
