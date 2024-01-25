from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser
from django.utils.translation import gettext_lazy as _



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'phone_number')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )



    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'first_name', 'last_name','phone_number', "password1", "password2"),
            },
        ),
    )


