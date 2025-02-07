"""
ASGI config for chat_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumers
import django
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

django.setup()

#add channel layers config
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
     "websocket": URLRouter([
        path("ws/chat/", consumers.ChatConsumer.as_asgi()),
    ]),
})
