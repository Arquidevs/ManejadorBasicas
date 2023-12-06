from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'id',
            'value',
            'variable',
        ]

        labels = {
            'id' : 'Id',
            'value' : 'Value',
            'variable' : 'Variable',
        }