from django.contrib.auth.models import User, UserManager
from django.db import models

class BlogUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicture = models.ImageField(default="noimage.png")