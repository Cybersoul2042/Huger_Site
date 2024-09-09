from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random, string, uuid, strgen

from .models import CustomUser, Project

# stringId  = uuid.uuid4()
# print("Secure unique string id", stringId)
# Output 0682042d-318e-45bf-8a16-6cc763dc8806

# Create your views here.

codes = []

def code_generator():
    code = strgen.StringGenerator("[\w\d]{16}").render()
    if code in codes:
        code_generator()
    else:
        return code
    

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
            
    return render(request, "main/index.html")

@csrf_exempt
def submit_project(request):
    
    if request.method == "POST":
        code = code_generator()
        username = request.POST["username"]
        major = request.POST["major"]
        year = request.POST["year"]
        subject = request.POST["p_name"]
        desc = request.POST["p_desc"]
        image = request.FILES.get("image")
        video = request.FILES.get("video")
        members = []
        for i in range(1, 4):
            if(request.POST[f'member{i}']):
                members.append(request.POST[f'member{i}'])

        project = Project(code = code, user = request.user.username, p_Leader=username, p_Major=major, p_Year=year, p_Subject=subject, p_Description=desc, p_Image=image, p_Video = video)
        project.save()
    
        for member in members:
            memberUser = CustomUser.objects.filter(email = member).first()
            project.p_Members.add(memberUser)

        project.save()

        return HttpResponseRedirect(reverse("submissions"))
    
    return render(request, "main/submit.html")

def submissions_view(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(user = request.user)
        
        return render(request, "main/submissions.html", {
            "projects": projects
        })
    
    return render(request, "main/submissions.html")

def project_view(request, ProjectCode):
    project = Project.objects.get(code = ProjectCode)
    return render(request, "main/project.html", {
        "project": project
    })
    

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
                user = CustomUser.objects.create_user(email, password)
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