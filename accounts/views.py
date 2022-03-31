from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import UpdateUserForm, UpdateBlogUser
from accounts.models import BlogUser


def signupView(request):
    userCreateForm = UserCreationForm(request.POST)
    if userCreateForm.is_valid():
        userCreateForm.save()
        username = userCreateForm.cleaned_data.get('username')
        password = userCreateForm.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        print(userCreateForm.errors)
    return render(request, 'signup.html', {'signupForm': userCreateForm})


def loginView(request):
    userLoginForm = AuthenticationForm(data=request.POST)
    if userLoginForm.is_valid():
        username = userLoginForm.cleaned_data.get('username')
        password = userLoginForm.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        print(userLoginForm.errors)
    return render(request, 'login.html', {'loginForm': userLoginForm})


@login_required(login_url='home')
def editProfileView(request):
    bu = BlogUser.objects.get(user = request.user)
    if request.method == 'POST':
        editUserForm = UpdateUserForm(request.POST, instance=request.user)
        editBlogUser = UpdateBlogUser(request.POST, request.FILES, instance=bu)
        if editUserForm.is_valid() and editBlogUser.is_valid():
            editBlogUser.save()
            editUserForm.save()
            return redirect('editProfile')
        else:
            print(editUserForm.errors)
    else:
        editUserForm = UpdateUserForm(instance=request.user)
        editBlogUser = UpdateBlogUser(request.POST, request.FILES, instance=bu)

    return render(request, 'editProfile.html', {'form': editUserForm, 'sform': editBlogUser})
