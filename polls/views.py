
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from .forms import QuestionForm, ChoiceFormSet

class VistaIndice(generic.ListView):
    #context_object_name y template_name son palabras reservada
    template_name = "polls/indice.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:10]

class VistaDetalle(generic.DetailView):
    #model y template_name son palabras reservada
    model = Question
    template_name = "polls/detalle.html"

class VistaResultados(generic.DetailView):
    #model y template_name son palabras reservada
    model = Question
    template_name = "polls/resultados.html"

def voto(request, id_pregunta):
    pregunta = get_object_or_404(Question, pk=id_pregunta)
    try:
        opcion_seleccionada = pregunta.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detalle.html",
                      {"question": pregunta, "error_message": "No elegiste una opción.", }, )
    else:
        opcion_seleccionada.votes = F("votes") + 1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse("polls:resultados", args=(id_pregunta,)))

def admin_encuesta(request, pk=None):
    pregunta = get_object_or_404(Question, pk=pk) if pk else None

    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=pregunta)
        formset = ChoiceFormSet(request.POST, instance=pregunta)

        if question_form.is_valid() and formset.is_valid():
            new_question = question_form.save(commit=False)

            "Valdiamos si es una nueva pregunta para asignarle fecha"
            if not new_question.pk:
                new_question.pub_date = timezone.now()

            new_question.save()
            formset.instance = new_question
            formset.save()
            return redirect('polls:gestion')
    else:
        question_form = QuestionForm(instance=pregunta)
        formset = ChoiceFormSet(instance=pregunta)

    context = {
        'question_form': question_form,
        'formset': formset,
        'form_title': 'Editar Preguntas y Respuestas' if pregunta else 'Crear Nueva Pregunta',
        'is_new': pregunta is None,
        'question': pregunta,
    }
    return render(request, 'polls/admin_encuestas.html', context)

def elimina_pregunta(request, pk):
    pregunta = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        pregunta.delete()
        return redirect('polls:gestion')

    context = {'question': pregunta}

    print("Tipo de dato del Contexto:", type(context))

    return render(request, 'polls/confirmar_elimina_pregunta.html', context)

class VistaGestion(generic.ListView):
    #context_object_name y template_name son palabras reservada
    template_name = "polls/gestion.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:10]

class VistaSoloResultados(generic.DetailView):
    #model y template_name son palabras reservada
    model = Question
    template_name = "polls/solo_resultados.html"





"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))

    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, Word. You're at the polls index.")


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise get_object_or_404("Question does not exist.")

    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
    # response = "You 're looking at the results of question %s."
    # return HttpResponse(response % question_id)

"""
