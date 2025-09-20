from django import forms

class PreguntaForm(forms.Form):
    texto_pregunta = forms.CharField(label="Tu pregunta", max_length=200)
    # Puedes añadir más campos para opciones si es un formulario de opción múltiple
    # Ejemplo: campo de opción múltiple
    opcion_elegida = forms.ChoiceField(
        choices=[('a', 'Opción A'), ('b', 'Opción B')],
        widget=forms.RadioSelect,
        label="Elige una opción"
    )