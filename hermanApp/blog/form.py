from django import forms
from .models import (
       Article,
       Comment,
)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
          'author',
          'title',
          'content',
          'image',
          'category'
        ] 

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = [
      'author','content','article',
    ]