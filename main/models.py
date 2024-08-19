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
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name="Leader_email")
    p_Leader = models.CharField(max_length = 256)
    p_Major = models.CharField(max_length = 64)
    p_Year = models.CharField(max_length = 64)
    p_Subject = models.CharField(max_length = 128)
    p_Description = models.TextField()
    p_Image = models.ImageField()
    p_Members = models.ManyToManyField(CustomUser)
    isChecked = models.BooleanField(default=False)

    def serialized(self):
        return self.p_Subject
    
    
