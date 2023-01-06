from django.urls import path
from MyBlogs import views


urlpatterns = [
    path('', views.index),
    path('Submit' , views.Submit),
    path('addPoll' , views.addPoll),
    path('search',views.search),
     
    
]
