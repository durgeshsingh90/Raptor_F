import yaml
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def load_yaml_data(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file.read())

def get_json_output(length, subfield, value, yaml_data):
    bm_data = yaml_data["BM060"]
    subfield_key = f"sf{subfield}"
    subfield_data = next((item[subfield_key] for item in bm_data if subfield_key in item), None)

    if not subfield_data:
        return None  # If subfield does not exist

    name = subfield_data["name"]
    format_val = subfield_data["format"]
    value_mapping = subfield_data.get("value", {})

    json_data = {
        "length": length,
        "subfield": subfield,
        "value": value,
        "name": name,
        "format": format_val
    }

  # Ensure 'value' is parsed as an integer if numeric
    mapped_value = value_mapping.get(int(value) if value.isdigit() else value, None)
    if mapped_value:
        json_data["value_description"] = mapped_value

    return json_data

def index(request):
    return render(request, 'BM60Parser/index.html')

def process_input(request):
    if request.method == 'POST':
        input_string = request.POST.get('user_input', '')
        input_string = input_string.rstrip('\r\n')
        yaml_data = load_yaml_data('BM60Parser/iso8583msgspec/BM60.yaml')
        results = []

        while len(input_string) > 0:
            length_field = int(input_string[:3])
            subfield = input_string[3:5]
            value_field = input_string[5:5 + length_field - len(subfield)]

            processed_data = get_json_output(length_field - len(subfield), subfield, value_field, yaml_data)
            if processed_data:
                results.append(processed_data)

            input_string = input_string[3 + length_field:]

        # Return JSON response if requested
        if request.GET.get('format') == 'json':
            json_response = {result['subfield']: result for result in results}
            return JsonResponse(json_response)

        # Otherwise, return HTML response
        return render(request, 'BM60Parser/index.html', {'user_input': request.POST['user_input'], 'results': results})

    else:
        return HttpResponse("Invalid Request")



