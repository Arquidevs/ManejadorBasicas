import json
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404, HttpResponse, JsonResponse
from facturacion.models.Paciente import Paciente
from facturacion.models.EstadoCuenta import EstadoCuenta
from facturacion.models.Servicio import Servicio
from facturacion.models.Manual_Tarifario import Manual_Tarifario
from django.core.exceptions import ObjectDoesNotExist
import pymongo
from manejador_basicas.manejador_basicas import settings

def crear_factura(request):
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



def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def crearManualTarifario (request):
    if request.method == 'POST':
        try: 
            json_data = json.loads(request.body)
            client= pymongo.MongoClient(settings.DB_NAME)
            db= client["facturacion"]
            collection = db["ManualTarifario"]
            data = {
                'idContrato': json_data.get('id', ''),
                'servicios': []
            }
            result = collection.insert_one(data)
            return JsonResponse({"mensaje": "Manual tarifario creado con éxito", "id": str(result.inserted_id)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            client.close()
    else:
        return HttpResponse("Método no permitido", status=405)
    
def crearServicio (request):
    if request.method == 'POST':
        try: 
            json_data = json.loads(request.body)
            client= pymongo.MongoClient(settings.DB_NAME)
            db= client["facturacion"]
            collection = db["Servicio"]
            data = {
                'id': json_data.get('id', ''),
                'tipo': json_data.get('tipo', ''),
                'descripcion': json_data.get('descripcion', '')
            }
            result = collection.insert_one(data)
            return JsonResponse({"mensaje": "Documento creado con éxito", "id": str(result.inserted_id)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            client.close()
    else:
        return HttpResponse("Método no permitido", status=405)
    
def addServicios(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            servicios_nuevos = json_data.get('servicios', [])
            id_contrato = json_data.get('id_contrato', '')
            nuevos_servicios = json_data.get('servicios', [])

            if not id_contrato or not nuevos_servicios:
                return JsonResponse({"error": "Se requieren 'id_contrato' y 'servicios' en el JSON"}, status=400)

            # Conectar a la base de datos
            client = pymongo.MongoClient(settings.DB_NAME)
            db = client["facturacion"]
            collection = db["ManualTarifario"]

            servicios_collection = db["Servicios"]
            servicios_existen = servicios_collection.find({"id_servicio": {"$in": servicios_nuevos}}).count() == len(servicios_nuevos)

            if not servicios_existen:
                return JsonResponse({"error": "Al menos uno de los servicios no existe en la colección de servicios"}, status=400)
            else:
                # Actualizar el documento existente
                filtro = {"idContrato": id_contrato}
                actualizacion = {"$addToSet": {"servicios": {"$each": nuevos_servicios}}}
                result = collection.update_one(filtro, actualizacion)

                if result.modified_count > 0:
                    return JsonResponse({"mensaje": "Servicios agregados con éxito"})
                else:
                    return JsonResponse({"mensaje": f"No se encontró un Manual Tarifario con id_contrato: {id_contrato}"}, status=404)

        except json.JSONDecodeError as json_error:
            return JsonResponse({"error": f"Error en el formato JSON: {json_error}"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            client.close()

    else:
        return HttpResponse("Método no permitido", status=405)