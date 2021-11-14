from django.shortcuts import render

# Create your views here.

from django.views import generic

class UserList(generic.TemplateView):
    template_name = "user-dashboard.html"
