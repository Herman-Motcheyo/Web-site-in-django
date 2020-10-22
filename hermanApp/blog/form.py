from django import forms
from .models import (
       Article,
       Comment,
)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'author', 'title', 'content', 'image', 'category'] 
        widgets = { 
          'author': forms.TextInput(attrs = {'class' : 'add-author' ,'placeholder' : '   Author of article  '}),
          'title': forms.TextInput(attrs = {'class' : 'add-title' , 'placeholder' : '   Title of article  '}),
          'content': forms.Textarea(attrs = { 'class' : 'add-content' ,'placeholder' : ' Tape content of article '}),
        }
  
        

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = [
      'author','content','article',
    ]
    widgets = { 
          'author': forms.TextInput(attrs = {'class' : 'add-author' ,'placeholder' : '   author name of comment  '}),
          'content': forms.Textarea(attrs = { 'class' : 'add-content' ,'placeholder' : ' write content on your comment '}),
        }