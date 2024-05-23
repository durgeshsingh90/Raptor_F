from django.urls import path
from .views import text_to_json_view

app_name = 'splunk2mango'

urlpatterns = [
    path('convert/', text_to_json_view, name='text_to_json'),
]
