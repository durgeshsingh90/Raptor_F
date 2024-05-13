# splunk2Json/urls.py

from django.urls import path
from . import views

app_name = 'splunk2Json'

urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process_input, name='process_input'),
]
