from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('footballista/', include('footballista.urls')),
    path('first_team/', include('footballista.urls')),
    path('second_teams/', include('footballista.urls')),
    path('teams/', include('footballista.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
