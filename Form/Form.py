from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
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
    return user

def SubmittedForms(request):
    user = [person.name for person in User.objects.all()]
    return user

def sendUserInfoToMail(userInfo):
    mail_template = render_to_string('EmailTemplate.html',{'user':userInfo})
    email = EmailMessage(
        'New User Registered',
        mail_template,
        'nisargmahyavanshi@gmail.com',
        ['nisargmahyavanshi@gmail.com'],
    )
    email.fail_silently = True
    email.send()