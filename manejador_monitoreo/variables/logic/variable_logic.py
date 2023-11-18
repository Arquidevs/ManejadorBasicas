from ..models import Variable


def get_variables():
    queryset = Variable.objects.all()
    return (queryset)


def create_variable(name):
    name = name[:100]
    variable, created = Variable.objects.get_or_create(name=name)
    if created:
        variable.save()
    return variable

def get_variable_by_name(name):
    try:
        variable = Variable.objects.get(name=name)
        return (variable)
    except:
        variable = None
        return (variable)