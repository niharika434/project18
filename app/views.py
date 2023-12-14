from django.shortcuts import render

# Create your views here.
from app.models import*
def display_topics(request):
    QLTO= Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)
def display_accesrecords(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecords':QLAO}
    return render(request,'display_accesrecords.html',d)
