from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'requiere_personalizacion', 'activo')
    list_filter = ('categoria', 'activo', 'requiere_personalizacion')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}
    
    # Esto permite editar precios directamente desde la lista, 
    # muy útil si cambias costos de insumos seguido
    list_editable = ('precio', 'activo')