
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import FriendForm
from users.forms import UserRegisterFormLanguage, UserRegisterFormAge, UserRegisterFormCommitment, UserRegisterFormSkills, UserRegisterFormLocation
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.db.models import GeometryField
from django.forms.models import model_to_dict
import json

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        formLanguage = UserRegisterFormLanguage(request.POST)
        formAge = UserRegisterFormAge(request.POST)
        formCommitment = UserRegisterFormCommitment(request.POST)
        formSkills = UserRegisterFormSkills(request.POST)
        formLocation = UserRegisterFormLocation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            formLanguage.save(commit=False)
            formAge.save(commit=False)
            formCommitment.save(commit=False)
            formSkills.save(commit=False)
            formLocation.save(commit=False)
            user.language_preference = formLanguage.cleaned_data.get('language_preference')
            user.age_range = formAge.cleaned_data.get('age_range')
            user.skill_level = formSkills.cleaned_data.get('skill_level')
            user.commitment_level = formCommitment.cleaned_data.get('commitment_level')
            user.location = formLocation.cleaned_data.get('location')
            user.save()
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        formLanguage = UserRegisterFormLanguage()
        form = UserRegisterForm()
        formAge = UserRegisterFormAge()
        formCommitment = UserRegisterFormCommitment()
        formSkills = UserRegisterFormSkills()
        formLocation = UserRegisterFormLocation()
    return render(request, 'users/register.html', {'form': form, 'formLanguage': formLanguage, 'formAge': formAge, 'formCommitment':formCommitment, 'formSkills':formSkills, 'formLocation':formLocation,} )

@login_required
def profile(request, pk=None):
    if pk:
        user = CustomUser.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

@login_required
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance = request.user)
    return render(request, 'users/update.html', {'form': form})



@login_required
def testfindfriends(request):
    radius = 5
    qLanguage = request.GET.get("language")
    qAge = request.GET.get("age")
    qUsername = request.GET.get("username")
    users = CustomUser.objects
    current_user = request.user
    users = CustomUser.objects.filter(location__dwithin=(current_user.location, Distance(km=radius))).exclude(id = request.user.id)
    if (qLanguage == "on" or qAge== "on" or qUsername):
        if qLanguage == "on":
            users = users.filter(language_preference=request.user.language_preference)
        if qAge == "on":
            users = users.filter(age_range=request.user.age_range)
        if qUsername:
            users = users.filter(username = qUsername)
        args = {'users':users}
        return render(request, 'users/testfindfriends.html', args)
    else:

        args = {'users':users}
        return render(request, 'users/testfindfriends.html', args)