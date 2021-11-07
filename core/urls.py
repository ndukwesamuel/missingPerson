from django.urls import path
from .views import (
    HometView, AboutView, Privacy, Terms, Complaints,
    Contact, missing_person,AdminDashboard,Admin_Missing_People_Report_all,
    Admin_Missing_People_Report_active, Admin_Missing_People_Report_found, Admin_Missing_People_Report_Pending,
    All_user_list, Create_missing_person,AdminUpdate,Enquiries_message,UserDashboard,
    EmergencyView, Howitwork, Found_people, Blogview, BlogDetail, Missing_people
     # UserDashboard,
    # Missing_People_Report
)


app_name = "core"

urlpatterns = [
    path('', HometView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('Privacy/', Privacy.as_view(), name='privacy'),
    path('Howitwork/', Howitwork.as_view(), name='Howitwork'),
    path('Found_people/', Found_people.as_view(), name='Found_people'),
    path('Missing_people/', Missing_people.as_view(), name='Missing_people'),
    path('Blogview/', Blogview.as_view(), name='Blogview'),
    path('BlogDetail/', BlogDetail.as_view(), name='BlogDetail'),
   
    path('Terms/', Terms.as_view(), name='Terms'),
    path('Complaints/', Complaints.as_view(), name='Complaints'),
    path('Contact/', Contact.as_view(), name='Contact'),
    path('missing_person/', missing_person.as_view(), name='missing_person'),

    # this is for admin dashborad
    path('AdminDashboard/', AdminDashboard.as_view(), name='AdminDashboard'),
    path('Admin_Missing_People_Report_all/', Admin_Missing_People_Report_all.as_view(), name='Admin_Missing_People_Report_all'), 
    path('Admin_Missing_People_Report_active/', Admin_Missing_People_Report_active.as_view(), name='Admin_Missing_People_Report_active'), 
    path('Admin_Missing_People_Report_found/', Admin_Missing_People_Report_found.as_view(), name='Admin_Missing_People_Report_found'), 
    path('Admin_Missing_People_Report_Pending/', Admin_Missing_People_Report_Pending.as_view(), name='Admin_Missing_People_Report_Pending'), 

    path('All_user_list/', All_user_list.as_view(), name='All_user_list'), 
    path('Create_missing_person/', Create_missing_person.as_view(), name='Create_missing_person'), 
    # admin dashbord end here Create_missing_person


    
    path('AdminUpdate/', AdminUpdate.as_view(), name='AdminUpdate'),  

    
    path('Enquiries_message/', Enquiries_message.as_view(), name='Enquiries_message'), 
    
    path('Emergency/', EmergencyView.as_view(), name='Emergency'),  



    # for UserDashboard 

    path('UserDashboard/', UserDashboard.as_view(), name='UserDashboard'),  
]
