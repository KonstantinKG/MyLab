from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings
from main.admin import core_site

urlpatterns = [
    path('admin/', core_site.urls),
    path('', include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
