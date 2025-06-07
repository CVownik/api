from django.contrib import admin
from .models import (
    CVInfo,
    Contact,
    ContactLinks,
    Experience,
    Duties,
    Education,
    Languages,
    SoftSkills,
    HardSkills,
    Intrests,
)

# Register your models here.


class CVInfoAdmin(admin.ModelAdmin):
    model = CVInfo

    list_display = ("name", "surname")

    list_filter = ("name", "surname")


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


class EducationAdmin(admin.ModelAdmin):
    model = Education

    list_display = ("cv_info_id", "institution", "degree")

    list_filter = ("institution", "degree", "start_date", "end_date")


class LanguagesAdmin(admin.ModelAdmin):
    model = Languages

    list_display = ("cv_info_id", "language")

    list_filter = ("language",)


class SoftSkillsAdmin(admin.ModelAdmin):
    model = SoftSkills

    list_display = ("cv_info_id", "skill")

    list_filter = ("skill",)


class HardSkillsAdmin(admin.ModelAdmin):
    model = HardSkills

    list_display = ("cv_info_id", "skill")

    list_filter = ("skill",)


class IntrestsAdmin(admin.ModelAdmin):
    model = Intrests

    list_display = ("cv_info_id", "interest")

    list_filter = ("interest",)


admin.site.register(CVInfo, CVInfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactLinks, ContactLinksAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Duties, DutiesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(SoftSkills, SoftSkillsAdmin)
admin.site.register(HardSkills, HardSkillsAdmin)
admin.site.register(Intrests, IntrestsAdmin)
