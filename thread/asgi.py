"""
ASGI config for thread project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
import os
from home.consumer import StudentsThread


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thread.settings')


ws_patterns = [
    path('ws/home/', StudentsThread.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns),
    "http": get_asgi_application(),
})