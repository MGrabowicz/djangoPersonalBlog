from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

def loginForm(request):
    userLoginForm = AuthenticationForm(data=request.POST)
    if request.method == 'POST':
        if userLoginForm.is_valid():
            username = userLoginForm.cleaned_data.get('username')
            password = userLoginForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            print(request.path)
            redirect('home')
        else:
            print(userLoginForm.errors)
    return {'loginForm': userLoginForm}
