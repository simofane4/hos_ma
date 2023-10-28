from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from appointment import views



urlpatterns = [
    path('create/',views.CreateAppointmentView.as_view(),name='create-appointment'),
    path('get',views.GetAppointmentView.as_view(),name='get-appointment'),
    path('update/<int:id>/',views.UpdateAppointmentView.as_view(),name='update-appointment'),
    path('delete/<int:id>/',views.DeleteAppointmentView.as_view(),name='delete-appointment'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)