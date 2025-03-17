from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir as rotas de professores do app
    path('', include('app.routes.professoresRoutes')),
    path('', include('app.routes.materiasRoutes')),   # Substitua pelo nome real do seu app
    path('', include('app.routes.diasdasemanaRoutes')),
    path('', include('app.routes.disponibilidadeRoutes')),
    path('', include('app.routes.adesaoRoutes')),
    path('', include('app.routes.turmaRoutes')),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)