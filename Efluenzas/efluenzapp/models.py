from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=1,choices=(('M','Male'),('F','Female')),blank=True)
    age = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
