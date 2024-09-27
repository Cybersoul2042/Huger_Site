from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from .models import CustomUser, Project, Member, Image, HugerVideo


class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    model = CustomUser
    list_display = ('ssn',"email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
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
    search_fields = ("email", 'ssn')
    ordering = ("ssn",)

class ProjectAdmin(ImportExportModelAdmin):
    model = Project
    list_display = ("user_name", "user_surname","p_Subject", "p_Major", "p_Year", "isChecked", )
    list_filter = ("user", "p_Major", "p_Year",)
    ordering = ("user",)

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ["project_model"]

    ordering = ("project_model",)

class MemberAdmin(ImportExportModelAdmin):
    model = Member
    list_display = ["project_model", "name", "surname", "major", "grade"]
    list_filter = ("major", "grade")

    search_fields = ("name", "surname", 'project_model')
    ordering = ("project_model",)

class HugerVideoAdmin(admin.ModelAdmin):
    model = HugerVideo
    list_display = ["name"]

    ordering = ("name",)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(HugerVideo, HugerVideoAdmin)