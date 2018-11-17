
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import FriendForm
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
import json

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, pk=None):
    if pk:
        user = CustomUser.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    context = {'latitude':user.location.y, 'longitude':user.location.x}
    return render(request, 'users/profile.html', {"location":json.dumps(context)})

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
    qLanguage = request.GET.get("language")
    qAge = request.GET.get("age")
    qUsername = request.GET.get("username")
    users = CustomUser.objects.exclude(id = request.user.id)


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