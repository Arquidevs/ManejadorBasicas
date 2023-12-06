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
    abnormal_measurements = Measurement.objects.filter(
        variable__name='heart-rate',
        anormal=True,
        value__lt=50,
    ).exclude(value__gt=120)

    if abnormal_measurements.exists():
        average_abnormal_heart_rate = abnormal_measurements.aggregate(Avg('value'))
        return average_abnormal_heart_rate['value__avg']
    else:
        return None