from django.db import models

class UserInfor(models.Model):
    user_name = models.CharField(max_length=50)
    user_birthdate = models.DateField('Birth-date')
    user_email = models.EmailField(max_length=100)
    user_contact = models.
