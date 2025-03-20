
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('', index,name='acceuil'),
]
