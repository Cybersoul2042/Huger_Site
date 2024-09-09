from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Project(models.Model):
    code = models.CharField(max_length=16)
    user = models.CharField(max_length=256)
    p_Leader = models.CharField(max_length = 256)
    p_Major = models.CharField(max_length = 64)
    p_Year = models.CharField(max_length = 64)
    p_Subject = models.CharField(max_length = 128)
    p_Description = models.TextField()
    p_Image = models.ImageField(upload_to='photos/', blank=True , default=None)
    p_Video = models.ImageField(upload_to='videos/', blank=True)
    p_Members = models.ManyToManyField(CustomUser, default=None)
    isChecked = models.BooleanField(default=False)

    def serialized(self):
        return self.p_Subject
    
    
