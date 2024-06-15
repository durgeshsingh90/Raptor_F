from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare_texts, name='compare_texts'),
]
