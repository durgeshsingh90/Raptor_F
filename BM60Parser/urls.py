from django.urls import path
from . import views

app_name = 'BM60Parser'

urlpatterns = [
    path('', views.index, name='index'),
    path('process_input/', views.process_input, name='process_input'),
]
