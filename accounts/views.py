from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'faculty':
                return redirect('faculty_dashboard')
            elif user.role == 'admin':
                return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')