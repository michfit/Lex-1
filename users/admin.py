from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm, UserUpdateForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['username', 'email', 'language_preference', 'age_range', 'commitment_level', 'skill_level', 'location']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

