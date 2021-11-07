from django.urls import path
from .views import (
            AboutView,CreateBlog,Bloglist

)


app_name = "blog"

urlpatterns = [
    path('create/', CreateBlog.as_view(), name='create'),
    path('', Bloglist.as_view(), name='blog'),
]