from django.shortcuts import render,reverse
from django.contrib import messages

# Create your views here.

from django.views import generic
from .forms import CustomUserCreationForm



class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


