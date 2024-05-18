# splunk2json/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .process_data import process_input_data

def process_data_view(request):
    if request.method == 'POST':
        input_lines = request.POST.get('input_data').splitlines()
        result = process_input_data(input_lines)
        return JsonResponse({'processed_data': result})
    return render(request, 'splunk2json/process_data_form.html')  # Ensure this matches the template path
