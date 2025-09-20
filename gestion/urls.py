from django.urls import path

from . import views

app_name = "gestion"
urlpatterns = [
    path("", views.gestion, name="gestion"),
    path('pregunta/', views.crear_pregunta, name='gestion')
    #path('exito/', views.pagina_exito, name='exito'),  # Define una vista de éxito

]
