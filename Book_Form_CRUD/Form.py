from django import forms
from .models import book

# This your model form for book

class addBook(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
        widgets = {
            'datePublished': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }