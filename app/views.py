from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate input fields (you can extend this with more validation)
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'index.html')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'index.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'index.html')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Log in the user after successful sign-up
        login(request, user)

        # Redirect to the home page or any other page
        return redirect('home')

    return render(request, 'index.html')
def home(request):
    return render (request,'index.html')