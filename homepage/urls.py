from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('SplunkRRN', views.SplunkRRN, name='SplunkRRN'),
    path('splunk2mango/', views.splunk2mango, name='splunk2mango'),
    path('json2yaml/', views.json2yaml, name='json2yaml'),  # New URL pattern

]
