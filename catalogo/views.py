from django.shortcuts import render, get_object_or_404, redirect
import urllib.parse
from .models import Producto, Categoria

def lista_productos(request, categoria_slug=None):
    categoria = None
    productos = Producto.objects.filter(activo=True)
    
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    
    categorias = Categoria.objects.all()
    
    return render(request, 'catalogo/lista_productos.html', {
        'categoria': categoria,
        'categorias': categorias,
        'productos': productos
    })

def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug, activo=True)
    
    if request.method == 'POST':
        texto_personalizado = request.POST.get('texto_personalizado', '')
        
        # Número de WhatsApp de destino (reemplaza con tu número con código de país, ej: 569XXXXXXXX)
        telefono = "56991976914" 
        
        # Construimos el mensaje formateado para tu taller
        mensaje = f"¡Hola! Me interesa encargar el producto *{producto.nombre}* (Precio: ${producto.precio} CLP).\nTexto para grabar con láser: *{texto_personalizado}*"
        
        import urllib.parse
        mensaje_encoded = urllib.parse.quote(mensaje)
        
        # URL oficial de WhatsApp para abrir chat directo
        whatsapp_url = f"https://wa.me/{telefono}?text={mensaje_encoded}"
        
        return redirect(whatsapp_url)

    return render(request, 'catalogo/detalle_producto.html', {'producto': producto})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        contacto_cliente = request.POST.get('email', '') # Correo o teléfono ingresado
        texto_mensaje = request.POST.get('mensaje', '')
        
        # Tu número de WhatsApp de destino (reemplaza con tu número real con código de país, ej: 569XXXXXXXX)
        telefono = "56991976914" 
        
        # Armamos el mensaje estructurado para tu taller
        mensaje = f"¡Hola! Me contacto desde la web de Don Señor Producciones.\n\n*Nombre:* {nombre}\n*Contacto:* {contacto_cliente}\n*Proyecto/Mensaje:* {texto_mensaje}"
        
        mensaje_encoded = urllib.parse.quote(mensaje)
        
        # URL oficial de WhatsApp para abrir chat directo
        whatsapp_url = f"https://wa.me/{telefono}?text={mensaje_encoded}"
        
        return redirect(whatsapp_url)
        
    return render(request, 'catalogo/contacto.html')