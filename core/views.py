from django.shortcuts import render, HttpResponse
from .models import Evento

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!!!!")

def eventos(request, titulo_evento):
    consulta = Evento.objects.get(titulo=titulo_evento)
    data = Evento.objects.get(titulo=titulo_evento).data_evento
    if consulta:
        return HttpResponse("{}, Data: {}". format(consulta, data))
    return HttpResponse("Evento não encontrado")