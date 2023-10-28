from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from ordonnance import views



urlpatterns = [
    path('create/',views.CreateOrdonnanceView.as_view(),name='create-ordonnance'),
    path('get',views.GetOrdonnanceView.as_view(),name='get-ordonnance'),
    path('update/<int:id>/',views.UpdateOrdonnanceView.as_view(),name='update-ordonnance'),
    path('delete/<int:id>/',views.DeleteOrdonnanceView.as_view(),name='delete-ordonnance'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)