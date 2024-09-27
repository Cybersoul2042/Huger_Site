from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random, string, uuid, strgen

from .models import CustomUser, Project, Member, Image, HugerVideo

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
    huger_videos = HugerVideo.objects.all()
    if request.user.is_authenticated:
        projects = Project.objects.filter(user = request.user)
        
        return render(request, "main/index.html", {
            "projects": projects,
            "videos": huger_videos
        })
            
    return render(request, "main/index.html", {
        "videos": huger_videos
    })

@login_required
def submit_project(request):
    
    if request.method == "POST":
        code = code_generator()
        id = len(Project.objects.all()) + 1
        user = request.user
        username = request.POST["name"]
        usersurname = request.POST["surname"]
        major = request.POST["major"]
        year = request.POST["year"]
        number = request.POST["phone-number"]
        subject = request.POST["p_name"]
        desc = request.POST["p_desc"]
        video = request.FILES.get("video")
        project = Project(id = id, code = code, user = user, user_name = username, user_surname = usersurname, p_Major=major, p_Number = number,p_Year=year, p_Subject=subject, p_Description=desc, p_Video = video)
        project.save()

        for i in range(1, 4):
            if(f'image{i}' in request.FILES):
                imgId = len(Image.objects.all()) + 1
                imgModel = Image(id = imgId, project_model = project, image=request.FILES.get(f'image{i}'))
                imgModel.save()
                project.p_Images.add(imgModel)
        
        project.save()

        for i in range(1, 4):
            if(f'member{i}-name' in request.POST):
                memName = request.POST[f'member{i}-name']
                memSurname = request.POST[f'member{i}-surname']
                memNum = request.POST[f'member{i}-number']
                memMajor = request.POST[f'member{i}-major']
                memGrade = request.POST[f'member{i}-grade']
                memId = len(Member.objects.all()) + 1
                memberModel = Member(id = memId, project_model = project, name = memName, surname = memSurname, phone_number = memNum, major=memMajor, grade=memGrade)
                memberModel.save()
                project.p_Members.add(memberModel)
            else: 
                break
        
        project.save()

        return HttpResponseRedirect(reverse("submissions"))
    
    return render(request, "main/submit.html")

@login_required
def submissions_view(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(user = request.user)
        images = []
        for project in projects:
            models = project.p_Images.all()
            images.append(models[0])
        members = Member.objects.all()
        
        return render(request, "main/submissions.html", {
            "projects": projects,
            "images": images,
            "members": members
        })
    
    return render(request, "main/submissions.html")
    

def login_view(request):
    if request.method == "POST":
        if 'email' in request.POST:
            ssn = request.POST["ssn"]
            email = request.POST["email"]
            password = request.POST["password"]
            emails = get_emails()
            if email in emails:
                return render(request, "main/login.html", {
                    "message": "یک اکانت با این ایمیل وجود دارد"
                })
            
            # Attempt to create new user
            try:
                user = CustomUser.objects.create_user(ssn, email, password)
                user.save()
            except IntegrityError:
                return render(request, "main/login.html",{
                    "message": "یک اکانت با این کد ملی وجود دارد"
                })

            
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # Attempt to sign user in
            ssn = request.POST["ssn"]
            password = request.POST["password"]
            user = authenticate(request, ssn=ssn, password=password)

            # Check if authentication successful
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "main/login.html", {
                    "message": "کد ملی یا/و رمز عبور اشتباه است"
                })
    else:
        return render(request, "main/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))