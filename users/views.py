from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm

def register(requests):
    if requests.method == "POST":
        form = UserRegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(requests, f"Your account has been Successfully created!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(requests, "users/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")


def profile(request):
    return render(request, "users/profile.html")
