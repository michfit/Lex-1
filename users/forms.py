from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
from itertools import chain
from .models import CustomUser, Language
from django import forms
from django.forms import ModelForm

LANGUAGES = (
    ('E', 'English'),
    ('S', 'Spanish'),
    ('P', 'Portuguese'),
    ('M', 'Mandarin'),
    ('R', 'Russian'),
    ('G', 'German'),
    ('H', 'Hindi'),
    ('M', 'Mandarin'),
    ('A', 'Arabic'),
    ('V', 'Vietnamese'),
    ('J', 'Japanese'),
    ('B', 'Bengali'),
)

class UserRegisterFormAge(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('age_range',)

class UserRegisterFormCommitment(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('commitment_level',)

class UserRegisterFormSkills(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('skill_level',)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class FriendForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('language_preference', 'age_range')