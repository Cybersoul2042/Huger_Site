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
    if request.user.is_authenticated:
        projects = Project.objects.filter(user = request.user)
        return render(request, "main/index.html", {
        "projects": projects
        })
    if request.method == "POST":
        username = request.POST["username"]
        major = request.POST["major"]
        year = request.POST["year"]
        subject = request.POST["p_name"]
        desc = request.POST["p_desc"]
        image = request.FILES.get("image")
        members = []
        for i in range(1, 4):
            if(request.POST[f'member{i}']):
                members.append(request.POST[f'member{i}'])

        project = Project(user = request.user, p_Leader=username, p_Major=major, p_Year=year, p_Subject=subject, p_Description=desc, p_Image=image)
        project.save()

        for member in members:
            memberUser = CustomUser.objects.filter(email = member).first()
            project.p_Members.add(memberUser)
        project.save()
            
    return render(request, "main/index.html")
    

def login_view(request):
    if request.method == "POST":
        if 'confirmation' in request.POST:
            email = request.POST["email"]
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            emails = get_emails()
            if email in emails:
                return render(request, "main/login.html", {
                    "message": "این ایمیل وجود دارد."
                })
            if confirmation != password:
                return render(request, "main/login.html", {
                    "message": "رمز عبور ها تطابق ندارند."
                })
            
            # Attempt to create new user
            try:
                user = CustomUser.objects.create_user(email, password, username)
                user.save()
            except IntegrityError:
                return render(request, "main/login.html",{
                    "message": "ایمیل قبلا استفاده شده است."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
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