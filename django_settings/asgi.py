import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import room.routing

from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings.settings')


# django_asgi_app = get_asgi_application()





application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": 
        AuthMiddlewareStack(
            URLRouter(
                room.routing.websocket_urlpatterns
            )
        )    
})






# application = get_asgi_application() было изначально
