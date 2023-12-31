from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('cabinet/', include('cabinet.urls')),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('assistant/', include('assistant.urls')),
    path('appointment/', include('appointment.urls')),
    path('acte/', include('acte.urls')),
    path('ordonnance/', include('ordonnance.urls')),
    path('medicament/', include('medicament.urls')),
    path('invoice/', include('invoice.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)