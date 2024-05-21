from django.urls import path
from .views import generate_data

app_name='sysgende'
urlpatterns = [
    path('generate/', generate_data, name='generate_data'),
]
