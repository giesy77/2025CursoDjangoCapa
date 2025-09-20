
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

def mapa(request):
    return render(request, "map/mapa.html")