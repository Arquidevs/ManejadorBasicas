from ..models import Variable


def get_variables():
    queryset = Variable.objects.all()
    return (queryset)


def create_variable(form):
    if form.is_valid():
        name = form.cleaned_data['name']
        name = name[:100]
        
        try:
            variable, created = Variable.objects.get_or_create(name=name)
            if created:
                variable.save()
                print(f"Variable creada: {variable}")
            else:
                print(f"Variable existente: {variable}")
            
            return variable
        except Exception as e:
            print(f"Error al crear la variable: {e}")
            return None
    else:
        print(f"Formulario no válido: {form.errors}")
        return None


def get_variable_by_name(name):
    try:
        variable = Variable.objects.get(name=name)
        return (variable)
    except:
        variable = None
        return (variable)