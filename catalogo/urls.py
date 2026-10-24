from django.urls import path
from .views import lista_productos, detalle_producto, contacto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('categoria/<slug:categoria_slug>/', lista_productos, name='lista_productos_por_categoria'),
    path('producto/<slug:slug>/', detalle_producto, name='detalle_producto'),
    path('contacto/', contacto, name='contacto'), # <-- Nueva ruta
]