from ..models import Measurement
from django.db.models import Avg

def get_measurements():
    queryset = Measurement.objects.all().order_by('-timestamp')[:10]
    return queryset

def create_measurement(form):
    measurement = form.save()
    measurement.save()
    return ()

def create_measurement_object(variable, value, unit):
    measurement = Measurement(variable=variable, value=value)
    measurement.save()
    return measurement

def getPromedioAnormal():
    average_abnormal_heart_rate = Measurement.objects.filter(variable__name='Heart-rate', anormal=True).aggregate(Avg('value'))
    
    return average_abnormal_heart_rate['value__avg'] 