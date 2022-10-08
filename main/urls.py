from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
   
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('team/',views.team,name="team"),
    path('login/',views.u_login,name="login"),
    path('signup/',views.u_signup,name="signup"),
]