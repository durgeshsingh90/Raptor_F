# bitmap_config/urls.py

from django.urls import path
from .views import import_page

urlpatterns = [
    path('import/', import_page, name='import_page'),
    # Add other URL patterns as needed
]
