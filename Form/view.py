from django.http import HttpResponse
from django.shortcuts import render
from . import Form

def index(request):
    return render(request,'Form.html')

def newUser(request):
    if request.method == 'POST':
        Form.FormSubmit(request)
        return HttpResponse("Registered")
    else:
        return HttpResponse("Please Enter a value")

