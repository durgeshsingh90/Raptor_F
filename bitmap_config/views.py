# bitmap_config/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ImportForm
from .models import Bitmap60Config  # Replace with the actual model name

# bitmap_config/views.py

# ... (other imports)

def import_page(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            json_data = form.cleaned_data['json_data']
            json_file = request.FILES.get('json_file')

            print(f'json_data: {json_data}')  # Add this line for debugging
            print(f'json_file: {json_file}')  # Add this line for debugging

            # Your logic for handling JSON data or file goes here

            your_model_instance = Bitmap60Config(json_data=json_data, json_file=json_file)
            try:
                your_model_instance.save()
                messages.success(request, 'Data successfully imported into the database.')

                saved_data = Bitmap60Config.objects.all()
                print(saved_data)  # Add this line for debugging

            except Exception as e:
                messages.error(request, f'Error saving data: {str(e)}')

            return redirect('import_page')
        else:
            messages.error(request, 'Invalid form data. Please correct the errors.')
    else:
        form = ImportForm()

    return render(request, 'bitmap_config/import_page.html', {'form': form})
