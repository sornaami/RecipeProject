"""RecipeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import register,signIn,signOut,create_profile,home,edit_profile,view_profile

urlpatterns = [
path("register",register,name="register"),
path("login",signIn,name="signIn"),
path("logout",signOut,name="signOut"),
path("profile",create_profile,name="create_profile"),
path("home",home,name="home"),
path("editprofile",edit_profile,name="edit_profile"),
path("viewprofile",view_profile,name="view_profile"),
]
