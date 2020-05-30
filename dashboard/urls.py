from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]
