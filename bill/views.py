import random

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'display.html')


def choice(request):
    n1 = (request.POST["txtno1"])
    n2 = (request.POST["txtno2"])
    n3 = (request.POST["txtno3"])
    l=[n1,n2,n3]
    n4=random.choice(l)
    res=n4
    return render(request,'display.html',{"res":res})