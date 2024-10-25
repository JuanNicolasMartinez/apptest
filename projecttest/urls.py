from django.contrib import admin
from django.urls import path, include
from newapp import views

urlpatterns = [
    path('tasks/', include('newapp.urls'))
]
