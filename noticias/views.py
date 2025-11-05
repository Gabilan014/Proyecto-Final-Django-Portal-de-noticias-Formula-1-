# noticias/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpRequest
from .models import Noticia

# Servicios / API
from .services import (
    get_driver_info,
    get_race_results,
    get_f1_news,
)

# ✅ Vista principal: muestra noticias desde la API
def noticias_api_list_view(request):
    noticias = get_f1_news()  # trae noticias desde la API
    return render(request, "noticias/lista.html", {"noticias": noticias})


# ✅ Vista detalle de noticia (solo si usás BD para noticias internas)
class NoticiaDetalleView(DetailView):
    model = Noticia
    template_name = "noticias/detalle.html"
    context_object_name = "noticia"


# ✅ Vista para mostrar info del piloto / resultados
def piloto_detalle_view(request, driver_id):
    driver = get_driver_info(driver_id)
    results = get_race_results(driver_id)

    return render(request, "noticias/piloto_detalle.html", {
        "driver": driver,
        "results": results
    })


# ✅ Vista por si querés buscar el piloto ?driver_id=4665
def piloto_detalle_search_view(request: HttpRequest):
    driver_id = request.GET.get("driver_id")
    driver = None
    results = []

    if driver_id:
        try:
            driver = get_driver_info(driver_id)
            results = get_race_results(driver_id)
        except Exception:
            pass

    return render(request, "noticias/piloto_detalle.html", {
        "driver": driver,
        "results": results,
        "driver_id_query": driver_id,
    })
