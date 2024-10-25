# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user_type == 'admin' and user.is_superuser:
                    login(request, user)
                    return redirect('admin_dashboard')  # Redirect to the admin page
                elif user_type == 'user' and not user.is_superuser:
                    login(request, user)
                    return redirect('user_dashboard')  # Redirect to user home page
                else:
                    messages.error(request, "Invalid credentials or user type.")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'accounts/staff_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

def home_view(request):
    return render(request, 'accounts/home.html')


def maintenance_view(request):
    return render(request, 'accounts/maintenance.html')

def report_view(request):
    return render(request, 'accounts/report.html')

def transaction_view(request):
    return render(request, 'accounts/transaction.html')


@login_required
def dashboard_view(request):
    if request.user.is_superuser: 
        return redirect('admin_dashboard') 
    else:
        return render(request, 'accounts/user_dashboard.html') 
    

def custom_logout_view(request):
    logout(request)  # Log out the user
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')