from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password  
from django.shortcuts import render, get_object_or_404
from .models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return redirect('home_view') 
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'userlogin.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password) 
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            User.objects.create(username=username, email=email, password=hashed_password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login_view') 
    
    return render(request,'register.html')


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated
    return render(request, 'home.html')
