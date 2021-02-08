from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField("Name",max_length=50)
    birth_date = models.CharField("Birth-date",max_length=50)
    email = models.CharField("Email",max_length=50)
    phone = models.CharField("Phone no.",max_length=50)
    gender = models.CharField("gender",default='male',max_length=10, choices=(("","Male"),("","Female")))
    remember_user = models.BooleanField("Remember User",default=False)
    registration_date = models.DateTimeField("Registered on", null=True)
    
    def __str__(self):
        return f'{["name: "+self.name,"BirthDate: "+self.birth_date,"email: "+self.email,"phone: "+self.phone,"gender: "+self.gender,"remember me: "+str(self.remember_user),"registered on: "+str(self.registration_date)]}'
    