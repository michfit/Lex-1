from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
from itertools import chain
from .models import CustomUser, Language

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'commitment_level', 'age_range', 'language_preference')
 
    language_preference = ModelMultipleChoiceField(queryset=Language.objects.all(), widget=Select2MultipleWidget)

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
