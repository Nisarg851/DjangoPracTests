from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from DataBase.models import User 

def FormSubmit(request):
    user = User()
    user.name = request.POST['name']
    user.birth_date = request.POST['date']
    user.email = request.POST['email']
    user.phone = request.POST['phone']
    user.gender = request.POST['gender']
    user.remember_user = "remember" in request.POST
    user.registration_date = timezone.now().date()
    user.save()