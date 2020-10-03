from django.shortcuts import render
from .models import cv

def index(request):
    queryset = cv.objects.all()
    context = {
        'project':queryset
    }
    return render(request,"cv/index.html" , context)


def detail(request ,id,**kwargs):
    pass
