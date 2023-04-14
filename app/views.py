from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic insertion is done successfully')
    return render(request,'insert_topic.html')
def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('webpage insertion is done successfully')
    return render(request,'insert_webpage.html')
def insert_accessrecords(request):
    if request.method=='POST':
       
        na=request.POST['na']
        WO=Webpage.objects.get_or_create(name=na)[0]
        WO.save()
        au=request.POST['au']
        da=request.POST['da']

       
        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()
        return HttpResponse('webpage insertion is done successfully')
    return render(request,'insert_accessrecords.html')