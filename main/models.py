from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(_('username'), max_length = 128)
    email = models.EmailField(_("email address"), unique = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Project(models.Model):
    p_Leader = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name="Project_Leader")
    p_Major = models.CharField(max_length = 64)
    p_SocialS = models.IntegerField()
    p_Number = models.IntegerField()
    p_Subject = models.CharField(max_length = 128)
    p_Image = models.ImageField()
    p_Description = models.TextField()
    p_Members = models.ManyToManyField(CustomUser, related_name="Project_Members")

    def serialized(self):
        return self.p_Subject
    
    
