from django import forms
from .models import Variable

# En el formulario
class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = ['name', 'description', 'unit']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 100:
            raise forms.ValidationError('El nombre de la variable no puede tener más de 100 caracteres.')
        return name