from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tramites', views.SeguimientoTramiteViewSet)
router.register(r'unidades', views.UnidadesViewSet)
router.register(r'tipostramite', views.TipoTramiteViewSet)
router.register(r'tramitetrazas', views.TramiteTrazaViewSet)

urlpatterns = [
    # path('unidades/', views.unidades, name='unidades'),
    # path('seguimientotramites/<str:unidad>', views.seguimientoTramite, name='seguimientoTramite'),
    # path('tramites/', views.tramiteFormView , name='tramites'),
    # path('saludo', views.index),
    path('', include(router.urls)),
    path('tramitesview/', views.SeguimientoTramiteCreateView.as_view()),
    path('tramites/cantidad/', views.tramite_count),
    path('unidades/activas/', views.unidades_activas),
    path('tramites/reporte/2023/', views.reporte_tramites_2023),
    path('tramite/trazas/<int:id>', views.tramite_traza),
]