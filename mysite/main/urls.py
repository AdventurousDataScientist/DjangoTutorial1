from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("<int:id>", views.list, name="list"),# if you just go to the localhost no extra arguments takes you to the index method in the views module, with the name index
    path("", views.home, name="home"),
    path("create", views.create, name="create")
]