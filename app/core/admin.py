"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    """User admin."""

    ordering = ['date_joined']
    list_display = ['last_name', 'first_name', 'email', 'phone_number']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
            }),
        (_('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'phone_number'
            )}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['last_login', 'date_joined']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'phone_number',
                'password1',
                'password2',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)