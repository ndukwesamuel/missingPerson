from django import forms
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, UsernameField
from BLOG.models import Blog_Post
from users_app.models import NewUser





        

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = "__all__"
        exclude = ('AuthorName',)

