from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'role')
    list_filter = ('is_active', 'is_admin')
    ordering = ('role','first_name')
    filter_horizontal = ()
    fieldsets = (
        ('Contact Info', {'fields': ('phone_number', 'email')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role')}),
        ('password', {'fields':('password',)})
    )
    add_fieldsets = (
        ('username and password', {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )


admin.site.register(models.User, CustomUserAdmin)