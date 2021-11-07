from django.contrib import admin

from core.models import  ComplaintsModel, EnquiriesModel, Missing_personsModel,REALMissing



class LeadAdmin(admin.ModelAdmin):
    # fields = (
    #     'first_name',
    #     'last_name',
    # )

    # list_display = ['first_name', 'last_name', 'age', 'email']
    # list_display_links = ['first_name']
    # list_editable = ['last_name']
    list_filter = ['status']
    # search_fields = ['first_name', 'last_name', 'email']





admin.site.register(ComplaintsModel)
admin.site.register(EnquiriesModel)
admin.site.register(Missing_personsModel)

admin.site.register(REALMissing, LeadAdmin)
# admin.site.register(test)