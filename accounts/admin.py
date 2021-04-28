from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from experts.models import ExpertProfile

User = get_user_model()


class ExpertProfileInline(admin.StackedInline):
    model = ExpertProfile
    can_delete = False
    verbose_name_plural = 'Expert Profile'


class CustomUserAdmin(UserAdmin):
    inlines = (ExpertProfileInline,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'first_name', 'last_name', 'email',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number', 'is_expert', 'balance', 'all_time_balance')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, CustomUserAdmin)
