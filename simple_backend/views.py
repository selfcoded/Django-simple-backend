from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, CustomForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out..')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'you have successfully registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def custom(request, num):
    records = list(Record.objects.values())
    recordId = []
    for record in records:
        recordId.append(record['id'])
    if num in recordId: 
        custom_record = Record.objects.get(id = num)
        return render(request, 'custom.html', {'custom_record': custom_record})
    else:
        messages.success(request, 'the record is not exist!')
        return redirect('home')


def delete_item(request, num):
    if request.user.is_authenticated:
        record = Record.objects.get(id = num)
        record.delete()
        messages.success(request, 'its been delete!')
        return redirect('home')
    else:
        messages.success(request, 'you need to be logged in!')
        return redirect('home')

def add_item(request):
    if request.user.is_authenticated:
        custom_form = CustomForm(request.POST or None)
        if request.method == 'POST':
            if custom_form.is_valid():
                custom_form.save()
                messages.success(request, 'record added')
                return redirect('home')
        return render(request, 'add.html', {'custom_form': custom_form})
    else: 
        messages.success(request, 'you must be logged in')
        return redirect('home')
    
def edit_item(request, num):
    item = Record.objects.get(pk = num)
    if request.method == 'POST':
        edit_form = CustomForm(request.POST,instance=item)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'record updated')
            return redirect('home')
    else:
        messages.success(request, 'hahahh')
        edit_form = CustomForm(instance=item)
    return render(request, 'edit.html', {'edit_form': edit_form})