import json
import traceback
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import pymongo
from manejador_basicas import settings
import requests

def crear_factura(request):
    if request.method == 'GET':
        try: 
            cedula = request.GET.get('cedula_paciente').strip()
            paciente=requests.get(f'http://35.193.9.218:3000/pacientes/{cedula}')
            contrato=requests.get(f'http://35.193.9.218:3000/contratos/{cedula}')
            estado=requests.get(f'http://35.193.9.218:3000/estado_cuenta/{cedula}')
            data_paciente=paciente.json()
            data_contrato=contrato.json()
            data_estado=estado.json()

            ##id ej 10102348473
            contrato=data_contrato["id"]

            client = pymongo.MongoClient(settings.DB_NAME)
            db = client["facturacion"]
            collection_mt = db["manualtarifario"]
            collection_servicios = db['Servicios']


            ## ej [16, 25 ,46]
            lista_servicios = [int(item["servicio"]) for item in data_estado]
            print(lista_servicios)
            factura=[]
            precioTotal=0

            for servicio in lista_servicios:
                resultado = collection_mt.find_one({'idContrato': int(contrato), 'idServicio': servicio})
                servicio_encontrado = collection_servicios.find_one({'id':servicio})
                factura.append(servicio_encontrado)
                print(resultado)
                precioTotal+=resultado['precio']
            
            print(factura, precioTotal)

            return JsonResponse({"factura": factura, "precio_total": precioTotal})

        except Exception as e:
            error_message = f"Error: {str(e)}\n\n{traceback.format_exc()}"
            return JsonResponse({"error": error_message}, status=500)
        


def getServiciosManualTarifario(idContrato):
    try:
        client = pymongo.MongoClient(settings.DB_NAME)
        db = client["facturacion"]
        collection = db["manualtarifario"]
        docs = collection.find()

        # Utiliza find_one() en lugar de find()
        manual_tarifario = collection.find_one({"idContrato": idContrato})
        print(manual_tarifario)
        if not manual_tarifario:
            return {"mensaje": f"No se encontró un Manual Tarifario con id_contrato: {idContrato}"}

        servicios = manual_tarifario.get('servicios', [])
        
        return {"idContrato": manual_tarifario['idContrato'], "servicios": servicios}

    except Exception as e:
        # Captura la excepción y devuelve un mensaje de error
        error_message = f"Error: {str(e)}\n\n{traceback.format_exc()}"
        return {"error": error_message}

    finally:
        client.close()


def lista_pacientes(request):
    if request.method == 'GET':
        response = requests.get('http://35.193.9.218:3000/pacientes/')
        
        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            try:
                # Intenta cargar los datos JSON si la respuesta no está vacía
                pacientes = response.json()
                return render(request, 'lista_pacientes.html', {'pacientes': pacientes})
            except ValueError as e:
                # Si la respuesta no es un JSON válido, maneja el error
                error_message = f"Error al decodificar JSON: {e}"
        
def crearManualTarifario (request):
    if request.method == 'POST':
        try: 
            json_data = json.loads(request.body)
            client= pymongo.MongoClient(settings.DB_NAME)
            db= client["facturacion"]
            collection = db["Manual_Tarifario"]
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