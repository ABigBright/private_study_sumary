from django.shortcuts import render
from django.http import HttpResponse
from service_tmp import models

# Create your views here.
def index(request):
    mod = models.UserModel.objects.all().first()
    print(mod.user,mod.passwd,mod.uid)
    return HttpResponse('hello django')