# input_app/views.py
import re
from django.shortcuts import render

def index(request):
    return render(request, 'BM61Parser/index.html')

def process_input(request):
    if request.method == 'POST':
        input_string = request.POST['user_input']
        # Clean up the input string
        input_string = input_string.strip()
        input_string = re.sub(r'\s+', ' ', input_string)

        results = []

        while len(input_string) > 0:
            length_field = int(input_string[:3])
            subfield = input_string[3:5]
            value_field = input_string[5:5 + length_field - 2]

            results.append({
                'length': length_field-len(subfield),
                'subfield': subfield,
                'value': f'<{value_field}>'
                # 'value': value_field
            })

            input_string = input_string[3 + length_field:]

        return render(request, 'BM61Parser/index.html',{'user_input': request.POST['user_input'] ,'results': results})

    else:
        return HttpResponse("Invalid Request")

