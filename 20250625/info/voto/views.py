from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Pregunta

def preguntas(request):
    # return HttpResponse("Hola mundo desde voto")
    list_preguntas = Pregunta.objects.order_by("-publicado_en")
    context = {"list_preguntas": list_preguntas}
    return render(request, "preguntas.html", context)

def detalle(request, pregunta_id):
    try:
        pregunta = Pregunta.objects.get(pk=pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404("No existe la pregunta que buscas!")
    
    context = {"pregunta": pregunta}
    return render(request, "detalle.html", context)