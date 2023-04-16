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
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST.get['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('webpage insertion is done successfully')
    return render(request,'insert_webpage.html',d)
def insert_accessrecords(request):
    LWO=Webpage.objects.all()
    d={'webpages':LWO}
    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        WO=Webpage.objects.get(name=na)
       
        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()
        return HttpResponse('accessrecord insertion is done successfully')
    return render(request,'insert_accessrecords.html',d)