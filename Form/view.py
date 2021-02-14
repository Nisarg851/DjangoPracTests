from django.http import HttpResponse
from django.shortcuts import render
from . import Form

def index(request):
    return render(request,'Form.html')

def newUser(request):
    if request.method == 'POST':
        userInfo = Form.FormSubmit(request)
        Form.sendUserInfoToMail(userInfo)
        return HttpResponse("Registered")
    else:
        return HttpResponse("Please Enter a value")

def list(request):
    users = Form.SubmittedForms(request)
    return render(request,'UserList.html', {'users':users})

