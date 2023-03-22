from django.shortcuts import render, redirect
from .models import CustomUser as User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def User_register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        password = make_password(password1)
        if User.objects.filter(email=email).first():
            messages.warning(request, 'Email Already exist!')
            return redirect('Login:register')
            
        if password1 != password2:
            messages.warning(request, 'password not match!')
            return redirect('Login:register')
        
        user = User (
            email = email,
            Full_name = full_name,
            phone = phone
        )
        user.set_password(password1)
        user.save()
        messages.success(request, 'Account succeefully created')
        return redirect('Login:login')
                
    return render(request, 'login/register.html')

def User_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('customar:home')
        else:
            messages.error(request, 'User not found! Something wrong')
            return redirect('Login:login')
        
    return render(request, 'login/login.html')

def User_logout(request):
    logout(request)
    return redirect('customar:home')

def Profile(request):
    context = {

    }
    return render(request, 'login/profile.html', context)