from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserStockAlert


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add the email field only if it's not already present in UserAdmin.fieldsets
    if not any('email' in fieldset[1]['fields'] for fieldset in UserAdmin.fieldsets):
        fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('email',)}),
        )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserStockAlert)