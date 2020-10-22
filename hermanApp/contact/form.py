from .models  import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fiels = ['name','email','message','suject']
        widgets = { 
        #  'author': forms.TextInput(attrs = {'class' : 'add-author' ,'placeholder' : '   Author of article  '}),
      #    'title': forms.TextInput(attrs = {'class' : 'add-title' , 'placeholder' : '   Title of article  '}),
      #    'content': forms.Textarea(attrs = { 'class' : 'add-content' ,'placeholder' : ' Tape content of article '}),
        }
  

