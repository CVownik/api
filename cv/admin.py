from django.contrib import admin
from .models import CVInfo, Contact, ContactLinks, Experience, Duties

# Register your models here.


class CVInfoAdmin(admin.ModelAdmin):
    model = CVInfo

    list_display = ("email", "name", "surname", "city", "country")

    list_filter = ("city", "country")


class ContactAdmin(admin.ModelAdmin):
    model = Contact

    list_display = ("cv_info_id", "telephone", "city", "email")

    list_filter = ("city",)


class ContactLinksAdmin(admin.ModelAdmin):
    model = ContactLinks

    list_display = ("contact_id", "name", "link")

    list_filter = ("name",)


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience

    list_display = ("cv_info_id", "position", "company")

    list_filter = ("position", "company", "start_date", "end_date")


class DutiesAdmin(admin.ModelAdmin):
    model = Duties

    list_display = ("experience_id", "description")

    list_filter = ("description",)


admin.site.register(CVInfo, CVInfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactLinks, ContactLinksAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Duties, DutiesAdmin)
