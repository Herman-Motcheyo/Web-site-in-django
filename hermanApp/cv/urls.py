from django.urls import path
from . import views

app_name ='cv'

urlpatterns = [
    path('',views.index ,name='index'),
    path('detail/<id>',views.detail,name='detail_project'),
]
