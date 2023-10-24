from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from acte import views



urlpatterns = [
    path('create/',views.CreateActeFaitView.as_view(),name='create-acte-fait'),
    path('get',views.GetActeFaitView.as_view(),name='get-acte-fait'),
    path('update/<int:id>/',views.UpdateActeFaitView.as_view(),name='update-acte-fait'),
    path('delete/<int:id>/',views.DeleteActeFaitView.as_view(),name='delete-acte-fait'),


    path('create/',views.CreateActeDemanderView.as_view(),name='create-acte-demander'),
    path('get',views.GetActeDemandertView.as_view(),name='get-acte-demander'),
    path('update/<int:id>/',views.UpdateActeDemanderView.as_view(),name='update-acte-demander'),
    path('delete/<int:id>/',views.DeleteActeDemanderView.as_view(),name='delete-acte-demander'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)