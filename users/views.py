
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import FriendForm
from users.forms import UserRegisterFormLanguage, UserRegisterFormAge, UserRegisterFormCommitment, UserRegisterFormSkills
from users.models import Friends

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        formLanguage = UserRegisterFormLanguage(request.POST)
        formAge = UserRegisterFormAge(request.POST)
        formCommitment = UserRegisterFormCommitment(request.POST)
        formSkills = UserRegisterFormSkills(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        formLanguage = UserRegisterFormLanguage()
        form = UserRegisterForm()
        formAge = UserRegisterFormAge()
        formCommitment = UserRegisterFormCommitment()
        formSkills = UserRegisterFormSkills()
    return render(request, 'users/register.html', {'form': form, 'formLanguage': formLanguage, 'formAge': formAge, 'formCommitment':formCommitment, 'formSkills':formSkills} )

@login_required
def profile(request, pk=None):
    if pk:
        user = CustomUser.objects.get(pk=pk)


    else:
        user = request.user
    friend = Friends.objects.get(current_user=request.user)
    friends = friend.users.all()
    args = {'user': user, 'friends':friends}
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
        friend, created = Friends.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        args = {'users': users, 'friends': friends}
        return render(request, 'users/testfindfriends.html', args)
    else:

        friend, created = Friends.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        args = {'users': users, 'friends': friends}
        return render(request, 'users/testfindfriends.html', args)

def change_friends(request, operation, pk):
    friend = CustomUser.objects.get(pk=pk)
    if operation == 'add':
        Friends.make_friend(request.user, friend)
        return redirect('findfriends')
    elif operation == 'remove':
        Friends.lose_friend(request.user, friend)
        return redirect('profile')
