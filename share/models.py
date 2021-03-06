from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.
class Content(models.Model):
     image = models.ImageField(upload_to='images/')
     title = models.CharField(max_length=200)
     relay = models.TextField()
     tag_set = models.ManyToManyField('Tag', blank=True)
     content = models.TextField()

     created_at = models.DateTimeField(auto_now_add = True)
     updated_at = models.DateTimeField(auto_now = True)
     
     def __str__(self):
          return self.title
          
class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)
   