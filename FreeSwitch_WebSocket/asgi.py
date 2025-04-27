import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import receiver.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freeswitch_audio.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            receiver.routing.websocket_urlpatterns
        )
    ),
})
