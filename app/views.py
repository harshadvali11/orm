from django.shortcuts import render
from app.models import *
# Create your views here.


def topic(request):
    #topics=Topic.objects.all()
    topics=Topic.objects.filter(topic_name='Music')
    return render(request,'displaytopic.html',context={'topics':topics})


def webpage(request):
    #webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(name='ronaldo')
    #webpages=Webpage.objects.order_by('url')
    webpages=Webpage.objects.all()[0:5]
    return render(request,'displaywebpage.html',context={'webpages':webpages})



def access(request):
    access=Access_Records.objects.all()
    return render(request,'displayaccess.html',context={'access':access})

