from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'role')
    list_filter = ()
    ordering = ('role','first_name')
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('phone_number',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    exclude = ('password',)

admin.site.register(models.User, CustomUserAdmin)