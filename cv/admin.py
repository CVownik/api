from django.contrib import admin
from .models import CVInfo

# Register your models here.

class CVInfoAdmin(admin.ModelAdmin):
    model = CVInfo

    list_display = ("email",
        "name",
        "surname",
        "city",
        "country")
    
    list_filter = ("city",
        "country")
    

admin.site.register(CVInfo, CVInfoAdmin)