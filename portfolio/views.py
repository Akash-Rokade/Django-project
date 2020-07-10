from django.shortcuts import render
from django.http import HttpResponse 
from .models import Items
# Create your views here.
def aboutme(request):
    item=Items.objects.all()

    return render(request,"aboutme.html",{'item':item})

def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")    