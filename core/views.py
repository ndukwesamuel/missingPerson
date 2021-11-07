from django.shortcuts import render,reverse

# Create your views here.

from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from core.forms import *

from core.models import *
from users_app.models import NewUser



class HometView(generic.CreateView):
    template_name = "index.html"
    form_class = REALMissingform

    def get_success_url(self):
        return reverse("core:home")
    


class AboutView(generic.TemplateView):
    template_name = "about.html"



class Privacy(generic.TemplateView):
    template_name = "privacy.html"

class Howitwork(generic.TemplateView):
    template_name = "Howitwork.html"


class Terms(generic.TemplateView):
    template_name = "terms.html"


class Contact(generic.CreateView):
    template_name = "enquiries.html"
    form_class = EnquiriesForm

    def get_success_url(self):
        return reverse("core:home")



class Complaints(generic.CreateView):
    template_name = "complaints.html"
    form_class = ComplaintsModelForm

    def get_success_url(self):
        return reverse("core:home")



class missing_person(generic.CreateView):
    template_name = "missing-person.html"
    form_class = Missing_personsModelForm

    def get_success_url(self):
        return reverse("core:home")





class Found_people(generic.TemplateView):
    template_name = "Found_people.html"
class Missing_people(generic.TemplateView):
    template_name = "Found_people.html"


class Blogview(generic.TemplateView):
    template_name = "Blogview.html"

class BlogDetail(generic.TemplateView):
    template_name = "BlogDetail.html"


class AdminDashboard(generic.ListView):
    template_name = 'Admin_dashboard.html'
    context_object_name = "nice"

    def get_queryset(self):
        queryset = {'REALMISSING':REALMissing.objects.all().count(),
                    'real':REALMissing.objects.all(),


                    'Active':REALMissing.objects.filter(status="active").count(),
                    'Pending':REALMissing.objects.filter(status="Pending").count(),
                    'Found':REALMissing.objects.filter(status="found").count(),
            
                    'Missing':Missing_personsModel.objects.all().order_by("-date_added"),
                    'EnquiriesModel':EnquiriesModel.objects.all().count(),
                    'ComplaintsModel':ComplaintsModel.objects.all().count(),
                    'Missing_personsModel':Missing_personsModel.objects.all().count()}

    
        return queryset


class Admin_Missing_People_Report_all(generic.ListView):
    template_name = "Missing_People_Report_dashboard.html"
    context_object_name = "all_people"

    def get_queryset(self):
        queryset = REALMissing.objects.all()

        return queryset

class Admin_Missing_People_Report_active(generic.ListView):
    template_name = "Missing_People_Report_dashboard_active.html"
    context_object_name = "all_people"

    def get_queryset(self):
        queryset = REALMissing.objects.filter(status="active")

        return queryset


class Admin_Missing_People_Report_found(generic.ListView):
    template_name = "Missing_People_Report_dashboard_found.html"
    context_object_name = "all_people"

    def get_queryset(self):
        queryset = REALMissing.objects.filter(status="found")

        return queryset


class Admin_Missing_People_Report_Pending(generic.ListView):
    template_name = "Missing_People_Report_dashboard_Pending.html"
    context_object_name = "all_people"

    def get_queryset(self):
        queryset = REALMissing.objects.filter(status="Pending")

        return queryset



class All_user_list(generic.ListView):
    template_name = "All_user_list.html"
    context_object_name = "all_people"

    def get_queryset(self):
        # queryset = REALMissing.objects.filter(status="Pending")
        # queryset = User.objects.all()
        # return queryset
        queryset = NewUser.objects.all()


        return queryset

    



class Create_missing_person(generic.CreateView):
    template_name = "Create_missing-person.html"
    form_class = REALMissingform

    def get_success_url(self):
        return reverse("core:home")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user.userprofile
        instance.save()
        self.product = instance
        return super(Create_missing_person, self).form_valid(form)



class AdminUpdate(generic.UpdateView):
    template_name = "AdminUpdate.html"
    form_class = userForm

    def get_success_url(self):
        return reverse("core:home")

    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user


# page 33 view
class Enquiries_message(generic.ListView):
    template_name = "Enquiries_message.html"
    context_object_name = "enquries"

    def get_queryset(self):
        queryset = EnquiriesModel.objects.all()
        return queryset



class EmergencyView(generic.ListView):
    template_name = "Emergency.html"
    context_object_name = "complains"

    def get_queryset(self):
        queryset = ComplaintsModel.objects.all()
        return queryset



class UserDashboard(generic.ListView):
    template_name = 'User_dashboard.html'
    context_object_name = "nice"

    def get_queryset(self):
        queryset = {'REALMISSING':REALMissing.objects.all().count(),
                    'real':REALMissing.objects.all(),


                    'Active':REALMissing.objects.filter(status="active").count(),
                    'Pending':REALMissing.objects.filter(status="Pending").count(),
                    'Found':REALMissing.objects.filter(status="found").count(),
            
                    'Missing':Missing_personsModel.objects.all().order_by("-date_added"),
                    'EnquiriesModel':EnquiriesModel.objects.all().count(),
                    'ComplaintsModel':ComplaintsModel.objects.all().count(),
                    'Missing_personsModel':Missing_personsModel.objects.all().count()}

    
        return queryset






