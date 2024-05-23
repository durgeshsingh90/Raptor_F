from django.urls import path
from .views import text_to_json_view

urlpatterns = [
    path('convert/', text_to_json_view, name='text_to_json'),
]
