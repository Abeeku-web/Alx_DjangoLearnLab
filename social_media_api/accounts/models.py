from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username

