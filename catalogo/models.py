from django.db import models
from django.utils.text import slugify
from cloudinary_storage.storage import MediaCloudinaryStorage

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0) # Usamos 0 si manejas precios en CLP
    imagen = models.ImageField(upload_to='productos/', storage=MediaCloudinaryStorage())
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    requiere_personalizacion = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    def precio_formateado(self):
        return f"{int(self.precio):_}".replace("_", ".")