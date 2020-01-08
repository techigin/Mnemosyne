from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import Signup_Form, Login_Form
from django.contrib.auth.models import User
# Create your views here.

def create_user_view(request):
    form = Signup_Form()

    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('register:trans_list')
    else:
        form = Signup_Form()

    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def login_user_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register:trans_list')



    return render(request, 'accounts/login.html')

def logout_user_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('accounts:login')
