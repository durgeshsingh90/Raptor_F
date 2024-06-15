from django.shortcuts import render

# Create your views here.
# MainWebsite/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/index.html')

def SplunkRRN(request):
    return render(request, 'homepage/SplunkRRN.html')

def splunk2mango(request):
    return render(request, 'homepage/splunk2mango.html')

def json2yaml(request):
    return render(request, 'homepage/json2yaml.html')