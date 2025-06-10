from django.contrib import admin
from .models import (
    CV,
    CVInfo,
    Contact,
    ContactLinks,
    Experience,
    Duties,
    Education,
    Languages,
    SoftSkills,
    HardSkills,
    Interests,
    Projects,
)

# Register your models here.


class CVAdmin(admin.ModelAdmin):
    model = CV

    list_display = ("user_id", "created_at")

    list_filter = ("created_at",)
    

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

    list_display = ("cv_id", "position", "company")

    list_filter = ("position", "company", "start_date", "end_date")


class DutiesAdmin(admin.ModelAdmin):
    model = Duties

    list_display = ("experience_id", "description")

    list_filter = ("description",)


class EducationAdmin(admin.ModelAdmin):
    model = Education

    list_display = ("cv_id", "institution", "degree")

    list_filter = ("institution", "degree", "start_date", "end_date")


class LanguagesAdmin(admin.ModelAdmin):
    model = Languages

    list_display = ("cv_id", "language")

    list_filter = ("language",)


class SoftSkillsAdmin(admin.ModelAdmin):
    model = SoftSkills

    list_display = ("cv_id", "skill")

    list_filter = ("skill",)


class HardSkillsAdmin(admin.ModelAdmin):
    model = HardSkills

    list_display = ("cv_id", "skill")

    list_filter = ("skill",)


class InterestsAdmin(admin.ModelAdmin):
    model = Interests

    list_display = ("cv_id", "interest")

    list_filter = ("interest",)


class ProjectsAdmin(admin.ModelAdmin):
    model = Projects

    list_display = ("cv_id", "name", "description")

    list_filter = ("name",)


admin.site.register(CV, CVAdmin)
admin.site.register(CVInfo, CVInfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactLinks, ContactLinksAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Duties, DutiesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(SoftSkills, SoftSkillsAdmin)
admin.site.register(HardSkills, HardSkillsAdmin)
admin.site.register(Interests, InterestsAdmin)
admin.site.register(Projects, ProjectsAdmin)
