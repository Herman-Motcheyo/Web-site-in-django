from django.shortcuts import render,redirect
from .form import  ContactForm

def index(request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid() :
                print("good operation")
                print("good operation")
                contact_form.save()
                return render(request,'contact/good.html')
               
        return  render(request,'contact/contact.html',{'form':contact_form })

def test(request):
        return  render(request,'contact/good.html')