import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def index(request):
    return render(request, 'BM60Parser/index.html')

def process_input(request):
    if request.method == 'POST':
        input_string = request.POST.get('user_input', '')
        # Clean up the input string
        input_string = input_string.rstrip('\r\n')

        results = []

        while len(input_string) > 0:
            length_field = int(input_string[:3])
            subfield = input_string[3:5]
            value_field = input_string[5:5 + length_field - len(subfield)]

            results.append({
                'length': length_field - len(subfield),
                'subfield': subfield,
                'value': value_field
            })

            input_string = input_string[3 + length_field:]

        # Prepare data for JSON response
        json_data = {}
        for result in results:
            json_data[result['subfield']] = result['value']

        # Return JSON response if requested
        if request.GET.get('format') == 'json':
            return JsonResponse(json_data)

        # Otherwise, return HTML response
        return render(request, 'BM60Parser/index.html', {'user_input': request.POST['user_input'], 'results': results})

    else:
        return HttpResponse("Invalid Request")
