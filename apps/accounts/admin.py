from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ("username",)
    list_display = (
        "username",
        "full_name",
        "is_staff",
        "created_at",
    )
    search_fields = (
        "username",
        "full_name",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
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
