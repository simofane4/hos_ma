from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from medicament import views



urlpatterns = [
    path('create/',views.CreateMedicamentView.as_view(),name='create-medicament'),
    path('get',views.GetMedicamentView.as_view(),name='get-medicament'),
    path('update/<int:id>/',views.UpdateMedicamentView.as_view(),name='update-medicament'),
    path('delete/<int:id>/',views.DeleteMedicamentView.as_view(),name='delete-medicament'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)