from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import (
    UserForm, 
    LoginForm,
)
from django.contrib.auth import (
    login,
    logout,
    # authenticate,
)
from django.contrib import messages

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            
            user=form.save()
            login(request, user)
            
            # form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, 'Congratulations, you have registered.')
            return redirect('home')    
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)

def user_logout(request):
    logout(request)
    messages.warning(request, 'You are now logged out.')
    return redirect('home')
    