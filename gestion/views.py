from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from django import forms
from .forms import PreguntaForm

def gestion(request):
    return render(request, "gestion/gestion.html", {})

def crear_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            # Procesar los datos validados (ej. guardar en la base de datos)
            print(form.cleaned_data)
            return redirect('exito') # Redirigir a una página de éxito
    else:
        form = PreguntaForm()
    return render(request, 'gestion/gestion.html', {'form': form})