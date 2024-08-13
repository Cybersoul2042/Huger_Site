from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random, string

from .models import CustomUser, Project

# Create your views here.

def get_emails():
    users = CustomUser.objects.all()
    emails = []
    for user in users:
        emails.append(user.email)

    return emails

def index(request):
    return render(request, "main/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "main/login.html", {
                "message": "ایمیل و/یا رمز عبور اشتباه است ."
            })
    else:
        return render(request, "main/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    emails = get_emails()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        if email in emails:
            return render(request, "main/register.html", {
                "message": "این ایمیل وجود دارد."
            })

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "main/register.html", {
                "message": "رمز های وارد شده تطابق ندارند ."
            })

        # Attempt to create new user
        try:
            user = CustomUser.objects.create_user(email, password, username)
            user.save()
        except IntegrityError:
            return render(request, "main/register.html",{
                "message": "ایمیل قبلا استفاده شده است."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "main/register.html")