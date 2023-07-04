from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'role')
    list_filter = ()
    ordering = ('role','first_name')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(models.User, CustomUserAdmin)