from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Project


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "is_staff", "is_active",)
    list_filter = ("email", "username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ("p_Leader", "user", "p_Subject", "isChecked",)
    
    ordering = ("p_Leader",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)