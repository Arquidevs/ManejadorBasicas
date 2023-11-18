from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VariableForm
from .logic.variable_logic import get_variables, create_variable
from django.http import HttpResponse


def variable_list(request):
    variables = get_variables()
    context = {
        'variable_list': variables
    }
    return render(request, 'variables.html', context)

def variable_create(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            # Obtén el valor del campo 'name' del formulario
            name = form.cleaned_data['name']

            # Recorta el nombre si es más largo de lo permitido
            name = name[:100]

            # Crea la variable con el nombre recortado
            variable = create_variable(name)

            if variable:
                messages.success(request, 'Variable creada exitosamente.')
                return redirect(reverse('variableList'))
            else:
                messages.error(request, 'Hubo un problema al crear la variable.')
        else:
            messages.error(request, 'Formulario no válido. Verifica los datos ingresados.')
    else:
        form = VariableForm()

    context = {'form': form}
    return render(request, 'variableCreate.html', context)