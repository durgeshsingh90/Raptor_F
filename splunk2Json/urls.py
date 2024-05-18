# splunk2json/urls.py

from django.urls import path
from .views import process_data_view

app_name = 'splunk2json'
urlpatterns = [
    path('process-data/', process_data_view, name='process_data'),
]
