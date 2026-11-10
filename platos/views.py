from rest_framework.decorators import api_view
from rest_framework.response import Response

from .datos import PLATOS


@api_view(['GET'])
def estado(request):
    return Response({"app": "Cafetería UTLA", "version": "1.0"})


@api_view(['GET', 'POST'])
def platos(request):
    if request.method == 'GET':
        return Response(PLATOS)

    nombre = request.data.get('nombre')
    precio = request.data.get('precio')

    if not nombre or precio is None:
        return Response({"error": "nombre y precio son obligatorios"}, status=400)

    nuevo = {
        "id": max(p["id"] for p in PLATOS) + 1,
        "nombre": nombre,
        "precio": precio,
    }
    PLATOS.append(nuevo)
    return Response(nuevo, status=201)


@api_view(['GET'])
def plato_detalle(request, id):
    for plato in PLATOS:
        if plato["id"] == id:
            return Response(plato)
    return Response({"error": "Plato no encontrado"}, status=404)