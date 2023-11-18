from django.shortcuts import render
from .forms import MeasurementForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_measurement import create_measurement, get_measurements, getPromedioAnormal

def measurement_list(request):
    measurements = get_measurements()
    average_heart_rate = getPromedioAnormal()
    
    context = {
        'measurements': measurements,
        'average_heart_rate': average_heart_rate,
    }
    
    return render(request, 'measurement.html', context)

def measurement_create(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            create_measurement(form)
            messages.add_message(request, messages.SUCCESS, 'Measurement create successful')
            return HttpResponseRedirect(reverse('measurementCreate'))
        else:
            print(form.errors)
    else:
        form = MeasurementForm()

    context = {
        'form': form,
    }

    return render(request, 'measurementCreate.html', context)