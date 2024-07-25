from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import SeguimientoTramite, Unidad, TramiteTraza, TipoTramite
from .forms import TramiteForm
from rest_framework import viewsets
from .serializers import SeguimientoTramiteSerializer, UnidadSerializer, ReporteTramites2023Serializer, TramiteTrazaSerializer, TipoTramiteSerializer, ReporteTramiteTrazaSerializer
from rest_framework import generics
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Hello, world! This is the home page.")

def seguimientoTramite(request, unidad):
    return HttpResponse(f"esta llegando la unidad {unidad}")

def unidades(request):
    post_descripcion = request.POST.get('descripcion')
    post_telefono = request.POST.get('telefono')
    if post_descripcion and post_telefono:
        q = Unidad(descripcion=post_descripcion, telefono=post_telefono)
        q.save()

    items = Unidad.objects.all()
    return render(request, 'form_unidades.html', {'unidades': items})

def tramites(request):

    filtro_gestion = request.GET.get('gestion')
    if filtro_gestion:
        items = SeguimientoTramite.objects.filter(gestionTramite=filtro_gestion)
    else:
        items = SeguimientoTramite.objects.all()

    return render(request, 'form_tramites.html', {'tramites': items})

def tramiteFormView(request):
    form = TramiteForm()
    tramite = None
    id_tramite = request.GET.get("id")

    if id_tramite:
        # tramite = SeguimientoTramite.objects.get(id=10011)
        tramite = get_object_or_404(SeguimientoTramite, id=id_tramite)
        form = TramiteForm(instance=tramite)

    if request.method == "POST":
        if tramite:
            form = TramiteForm(request.POST, instance=tramite)
        else:
            form = TramiteForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_tramites.html", {"form": form})

class SeguimientoTramiteViewSet(viewsets.ModelViewSet):
    queryset = SeguimientoTramite.objects.all()
    serializer_class = SeguimientoTramiteSerializer

class SeguimientoTramiteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = SeguimientoTramite.objects.all()
    serializer_class = SeguimientoTramiteSerializer

class UnidadesViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class TramiteTrazaViewSet(viewsets.ModelViewSet):
    queryset = TramiteTraza.objects.all()
    serializer_class = TramiteTrazaSerializer

class TipoTramiteViewSet(viewsets.ModelViewSet):
    queryset = TipoTramite.objects.all()
    serializer_class = TipoTramiteSerializer


@api_view(['GET'])
def tramite_count(request):
    """
    Cuenta la cantidad de __Trámites__
    """
    try: 
        cantidad = SeguimientoTramite.objects.count()
        return JsonResponse(
            {
                'Cantidad': cantidad
            },
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'Error': str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def unidades_activas(request):
    """
    __Unidades__ activas
    """
    try:
        unidadesActivas = Unidad.objects.filter(estado='ac')
        return JsonResponse(
            UnidadSerializer(unidadesActivas, many=True).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'Error': str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def reporte_tramites_2023(request):
    """
    Reporte de cantidad de __Trámites__
    """
    try:
        tramites = SeguimientoTramite.objects.filter(gestionTramite=2023)
        cantidad = tramites.count()
        return JsonResponse(
            ReporteTramites2023Serializer({
                "cantidad" : cantidad,
                "tramites": tramites 
            }).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'Error': str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def tramite_traza(request, id):
    """
    Trazas del tramite __Trámites__
    """
    try:
        # id_tramite = request.GET.get("id")
        id_tramite = id
        tramite = get_object_or_404(SeguimientoTramite, id=id_tramite)
        trazas = TramiteTraza.objects.filter(seguimientoTramite_id=id_tramite)
        return JsonResponse(
            ReporteTramiteTrazaSerializer({
                "tramite" : tramite,
                "tramiteTrazas": trazas 
            }).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'Error': str(e)
            },
            safe=False,
            status=400
        )