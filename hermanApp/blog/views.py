from django.shortcuts import render,redirect
from django import forms
from .models import(
         Article,
         Comment,
         Category,
) 
from .form import (
    ArticleForm,
    CommentForm
)


def index(request):
    article = Article.objects.all()
    return render(request,'blog/index.html',{'article':article})

def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/blog/')
    context = {
        'form' : form,
    }
    return render(request,'blog/add.html',context)

def show_article(request,id, **kwargs):
    article = Article.objects.get(pk = id)
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        comment.save()
        return redirect('show_article',pk=id )
    
    comments = Comment.objects.filter(article=article)
    context  = {
        'form':comment,
        'comment':comments,
        'article':article
    }
    return render(request, 'blog/show.html',context)
