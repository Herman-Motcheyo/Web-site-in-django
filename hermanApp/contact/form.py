from .models  import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','suject','email','message']
        widgets = { 
          'name': forms.TextInput(attrs = {'class' : 'add-author' ,'placeholder' : '   Your name  '}),
          'suject': forms.TextInput(attrs = {'class' : 'add-title' , 'placeholder' : '   Subject  '}),
         'message': forms.Textarea(attrs = { 'class' : 'add-content' ,'placeholder' : ' Tape content here'}),
        }
  

