# splunk2Json/views.py

from django.shortcuts import render
from django.http import HttpResponse
import json
from datetime import datetime, timedelta

def index(request):
    return render(request, 'splunk2Json/index.html')

def process_input(request):
    if request.method == 'POST':
        input_lines = request.POST.get('user_input', '').split('\n')
        input_data = '\n'.join(input_lines)

        index_pattern = r'in\[ *(\d+): *\]'
        matches = re.findall(r'in\[ *(\d+): *\]<(.+?)>', input_data)
        indices_to_concatenate = [7, 43]
        current_date = datetime.now()
        json_data = {"mti": 100, "data_elements": {}}

        for match in matches:
            index = match[0]
            value = match[1]
            if int(index) == 129:
                continue
            if int(index) in indices_to_concatenate:
                if f"DE{index.zfill(3)}" in json_data["data_elements"]:
                    json_data["data_elements"][f"DE{index.zfill(3)}"] += value
                else:
                    json_data["data_elements"][f"DE{index.zfill(3)}"] = value
            elif int(index) == 3:
                value = value.ljust(6, '0')
                json_data["data_elements"][f"DE{index.zfill(3)}"] = value
            elif int(index) == 4:
                value = str(int(value))
                json_data["data_elements"][f"DE{index.zfill(3)}"] = value
            # Other processing logic for different indices...
        
        if "DE007" in json_data["data_elements"]:
            value = json_data["data_elements"]["DE007"]
            json_data["data_elements"]["DE007"] = value.zfill(10)

        json_output = json.dumps(json_data, indent=4)
        return HttpResponse(json_output, content_type='application/json')
    else:
        return HttpResponse("Invalid Request")
