from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    ssn = models.CharField(_("social security number"), max_length=10, unique = True)
    email = models.EmailField(_("email address"))

    USERNAME_FIELD = "ssn"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.ssn
    
class Member(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    project_model = models.ForeignKey("Project", related_name = "assigned_project",on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    major = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)

    def serialized(self):
        return self.name
    
class Image(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    project_model = models.ForeignKey("Project", related_name = "assigned_image_project", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', blank=True , default=None)

class Project(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    code = models.CharField(max_length=16)
    user = models.ForeignKey("CustomUser", related_name = "project_leader", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=128)
    user_surname = models.CharField(max_length=128)
    p_Major = models.CharField(max_length = 64)
    p_Number = models.CharField(max_length=11)
    p_Year = models.CharField(max_length = 64)
    p_Subject = models.CharField(max_length = 128)
    p_Description = models.TextField()
    p_Video = models.FileField(upload_to='videos/', blank=True, default=None)
    p_Images = models.ManyToManyField("Image", default=None)
    p_Members = models.ManyToManyField("Member", default=None)
    isChecked = models.BooleanField(default=False)

    def __str__(self):
        return self.p_Subject
    
class HugerVideo(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField(max_length=256)
    num = models.IntegerField(default=1)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name
    
    
