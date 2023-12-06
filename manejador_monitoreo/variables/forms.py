from django import forms
from .models import Variable

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = [
            'name', 'description', 'unit'
        ]
        labels = {
            'name': 'Name', 'description': 'Description', 'unit': 'Unit'
        }