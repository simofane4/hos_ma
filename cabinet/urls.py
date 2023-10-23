from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from cabinet import views



urlpatterns = [
    path('create/',views.CreateCabinetView.as_view(),name='create-cabinet'),
    path('get',views.GetCabinetView.as_view(),name='get-cabinet'),
    path('update/<int:id>/',views.CabinetUpdateView.as_view(),name='update-cabinet'),
    path('delete/<int:id>/',views.CabinetDeleteView.as_view(),name='delete-cabinet'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)