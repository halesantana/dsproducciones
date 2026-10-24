"""
WSGI config for ventas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ventas.settings')

application = get_wsgi_application()

# Esto le enseña a WhiteNoise a servir también las imágenes de la carpeta media en producción
application = WhiteNoise(application)
application.add_files(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media'), prefix='media/')
