# miniportal/urls.py

from django.contrib import admin
from django.urls import path
from noticias.views import noticias_api_list_view, piloto_detalle_view, piloto_detalle_search_view, NoticiaDetalleView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Página de inicio → muestra las noticias obtenidas de la API
    path("", noticias_api_list_view, name="home"),

    # Detalle de noticia (solo si usás modelo Noticia)
    path("noticia/<int:pk>/", NoticiaDetalleView.as_view(), name="noticia_detalle"),

    # Piloto por ID en URL
    path("piloto/<int:driver_id>/", piloto_detalle_view, name="piloto_detalle"),

    # Buscar piloto desde un formulario con ?driver_id=4665
    path("piloto/buscar/", piloto_detalle_search_view, name="piloto_detalle_search"),
]
