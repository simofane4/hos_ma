from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from assistant import views



urlpatterns = [
    path('create/',views.CreateAssistantView.as_view(),name='create-assistant'),
    path('get',views.GetAssistantView.as_view(),name='get-assistant'),
    path('update/<int:id>/',views.UpdateAssistantView.as_view(),name='update-assistant'),
    path('delete/<int:id>/',views.DeleteAssistantView.as_view(),name='delete-assistant'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)