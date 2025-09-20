from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.VistaIndice.as_view(), name="indice"),
    path("<int:pk>/", views.VistaDetalle.as_view(), name="detalle"),
    path("<int:pk>/resultados/", views.VistaResultados.as_view(), name="resultados"),
    path("<int:id_pregunta>/voto/", views.voto, name="voto"),
    path("gestion/", views.VistaGestion.as_view(), name="gestion"),
    path("<int:pk>/solo_resultados/", views.VistaSoloResultados.as_view(), name="solo_resultados"),

    path('manage/', views.admin_encuesta, name='admin_encuesta_crear'),
    path('manage/<int:pk>/', views.admin_encuesta, name='admin_encuesta_editar'),
    path('delete/<int:pk>/', views.elimina_pregunta, name='elimina_pregunta'),


    # path("", views.index, name="index"),
    # path("specifics/<int:question_id>/", views.details, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote")
]
