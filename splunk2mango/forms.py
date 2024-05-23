from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Sample:\n in[  3: ]<0> \n in[  4: ]<123> '}),
        label='Enter text'
    )
