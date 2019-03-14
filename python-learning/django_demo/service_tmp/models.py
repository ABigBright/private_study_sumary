from django.db import models

# Create your models here.

class UserModel(models.Model):
    uid = models.IntegerField()
    user = models.CharField(max_length=12)
    passwd = models.CharField(max_length=12)
