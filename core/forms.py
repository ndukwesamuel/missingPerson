from django import forms
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, UsernameField
from core.models import  Missing_personsModel, ComplaintsModel, EnquiriesModel, REALMissing 
from users_app.models import NewUser




class EnquiriesForm(forms.ModelForm):
    class Meta:
        model = EnquiriesModel
        fields = "__all__"

class Missing_personsModelForm(forms.ModelForm):
    class Meta:
        model = Missing_personsModel
        fields = "__all__"



class ComplaintsModelForm(forms.ModelForm):
    class Meta:
        model = ComplaintsModel
        fields = "__all__"
        

class REALMissingform(forms.ModelForm):
    class Meta:
        model = REALMissing
        fields = "__all__"
        exclude = ('user',)

class userForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('full_name', 'email', 'phone',)
