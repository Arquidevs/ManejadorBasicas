from django.shortcuts import render
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from facturacion.models.Paciente import Paciente
from facturacion.models.EstadoCuenta import EstadoCuenta
from facturacion.models.Servicio import Servicio
from facturacion.models.Manual_Tarifario import Manual_Tarifario
from facturacion.models.Contrato import Contrato
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from manejador_basicas.auth0backend import getRole

@login_required
def crear_factura(request):
    role= getRole(request)
    if role=="Administrativo":
        if request.method == 'GET':
            cedula_paciente = request.GET.get('cedula_paciente').strip()

            try:
                paciente = Paciente.objects.get(id__iexact=cedula_paciente)
                servicios = EstadoCuenta.objects.filter(paciente=paciente).values('servicio')

                factura = []
                precio_total = 0

                for servicio in servicios:
                    manual_tarifario = Manual_Tarifario.objects.get(id_servicio=servicio['servicio'], id_contrato=paciente.id_contrato)
                    servicio = Servicio.objects.get(id=servicio['servicio'])

                    precio = manual_tarifario.precio
                    factura.append((servicio.descripcion, precio))
                    precio_total += precio

                return render(request, 'resultado_consulta.html', {
                    'id_factura': paciente.id,  # ID del paciente
                    'servicios_y_precios': factura,
                    'precio_total': precio_total  # Precio total
                })

            except ObjectDoesNotExist:
                raise Http404("El paciente no existe")
    else:
        return HttpResponse("Unauthorized User")



@login_required
def lista_pacientes(request):
    role= getRole(request)
    if role=="Administrativo":
        pacientes = Paciente.objects.all()
        return render(request, 'lista_pacientes.html', {'pacientes': pacientes})
    else:
        return HttpResponse("Unauthorized User")




