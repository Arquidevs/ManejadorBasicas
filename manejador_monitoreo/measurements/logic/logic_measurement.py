from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_measurement(form):
    measurement = form.save()
    measurement.save()
    return ()

def create_measurement_object(variable, value, unit):
    measurement = Measurement(variable=variable, value=value)
    measurement.save()
    return measurement