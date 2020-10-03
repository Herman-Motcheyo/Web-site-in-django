from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path('', views.index, name="index"),
    path('add/',views.create_article,name="add_article"),
    path("show/<id>",views.show_article,name = "show_article"),
]