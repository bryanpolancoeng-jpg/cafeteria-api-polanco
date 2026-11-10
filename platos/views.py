from rest_framework.decorators import api_view
from rest_framework.response import Response

from .datos import PLATOS


@api_view(['GET'])
def estado(request):
    return Response({"app": "Cafetería UTLA", "version": "1.0"})


@api_view(['GET'])
def platos(request):
    return Response(PLATOS)


@api_view(['GET'])
def plato_detalle(request, id):
    for plato in PLATOS:
        if plato["id"] == id:
            return Response(plato)
    return Response({"error": "Plato no encontrado"}, status=404)