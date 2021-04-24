from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user =models.OneToOneField(User , on_delete=models.CASCADE)
    addr=models.CharField(max_length=70)
    addr2=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    zip_number=models.CharField(max_length=70)
    def __str__(self):
        return self.user.username
  