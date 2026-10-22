from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ("email",)
    list_display = (
        "email",
        "full_name",
        "is_staff",
        "created_at",
    )
    search_fields = (
        "email",
        "full_name",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("Dates info", {"fields": ("last_login",)}),
    )


admin.site.register(User, CustomUserAdmin)
