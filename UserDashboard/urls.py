from django.urls import path
from .views import (UserList,)


app_name = "userdashboard"

urlpatterns = [
    path('', UserList.as_view(), name='UserList'),

]
