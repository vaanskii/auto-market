from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import activateEmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activateEmail/', activateEmail, name='activate_email'),
    path('api/', include('account.urls')),
    path('api/', include('cars.urls')),
    path('api/', include('filters.urls')),
    path('api/', include('vin.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
