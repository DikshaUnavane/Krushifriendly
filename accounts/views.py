from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Payment

@login_required
def payment_history(request):
    payments = Payment.objects.all().order_by('-payment_date')  # instead of filter(user=request.user)
    return render(request, 'accounts/payment_history.html', {'payments': payments})




def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Account created successfully! Please login.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("step6")  # you can create dashboard later
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

from django.shortcuts import render

def home_after_login(request):
    return render(request, 'rental/step6.html')  # path to your template
