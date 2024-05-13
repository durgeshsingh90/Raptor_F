from django.shortcuts import render

# Create your views here.
# MainWebsite/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/index.html')