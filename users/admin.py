from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, HR, Premium
from .forms import CustomUserCreationForm


class UsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = (
        "email",
        "name",
        "surname",
        "hr_role",
        "premium_role",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "surname",
                    "hr_role",
                    "premium_role",
                    "password",
                    "hr_expires_at",
                    "premium_expires_at",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "surname",
                    "hr_role",
                    "premium_role",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
        (
            "HR Details (for HR Role)",
            {
                "fields": (
                    "company_name",
                    "company_nip",
                    "telephone",
                    "city",
                    "street",
                    "number_street",
                    "postcode",
                )
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class HRAdmin(admin.ModelAdmin):
    model = HR
    list_display = ("user", "company_name")


class PremiumAdmin(admin.ModelAdmin):
    model = Premium
    list_display = ("user",)


admin.site.register(CustomUser, UsersAdmin)
admin.site.register(HR, HRAdmin)
admin.site.register(Premium, PremiumAdmin)
