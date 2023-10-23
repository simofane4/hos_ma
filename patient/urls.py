from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from patient import views






urlpatterns = [
    path('create/',views.CreatePatientView.as_view(),name='create-patient'),
    path('get',views.GetPatientView.as_view(),name='get-patient'),
    path('update/<int:id>/',views.UpdatePatientView.as_view(),name='update-patient'),
    path('delete/<int:id>/',views.DeletePatientView.as_view(),name='delete-patient'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)