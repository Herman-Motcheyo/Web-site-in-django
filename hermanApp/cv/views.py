from django.shortcuts import render

def index(request):
    return render(request,"cv/index.html")


def detail(request ,id):
    pass
