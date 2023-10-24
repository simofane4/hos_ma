from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from doctor import views



urlpatterns = [
    path('create/',views.CreateDoctorView.as_view(),name='create-doctor'),
    path('get',views.GetDoctorView.as_view(),name='get-doctor'),
    path('update/<int:id>/',views.UpdateDoctorView.as_view(),name='update-doctor'),
    path('delete/<int:id>/',views.DeleteDoctorView.as_view(),name='delete-doctor'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)