from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # validation of the users
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have logged in!')
            return redirect('home')
        else:
            messages.success(request, 'there was an error....')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out..')
    return redirect('home')