from django.urls import path

from . import views

urlpatterns =[
    path('',views.about,name='index'),
    path('about',views.about,name='about'),
    path('index',views.above,name='abt'),
]