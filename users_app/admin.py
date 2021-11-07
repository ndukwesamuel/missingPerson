from django.contrib import admin

# Register your models here.

from users_app.models import NewUser


admin.site.register(NewUser)