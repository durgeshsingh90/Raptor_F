# bitmap_config/forms.py

from django import forms
from .models import Bitmap60Config  # Update the import here

class ImportForm(forms.ModelForm):
    class Meta:
        model = Bitmap60Config  # Update the model name here
        fields = '__all__'
