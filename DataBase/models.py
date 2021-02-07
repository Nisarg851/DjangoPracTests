from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField("Name",max_length=50)
    birth_date = models.CharField("Name",max_length=50)
    email = models.CharField("Name",max_length=50)
    phone = models.CharField("Name",max_length=50)
    gender = models.CharField("Gender",default='male',max_length=10)
    remember_user = models.BooleanField("Remember User",default=False)
    registration_date = models.DateTimeField("Registered on", null=True)