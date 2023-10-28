from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from invoice import views



urlpatterns = [
    path('create/',views.CreateInvoiceView.as_view(),name='create-invoice'),
    path('get/',views.GetInvoiceView.as_view(),name='get-invoice'),
    path('update/<int:id>/',views.UpdateInvoiceView.as_view(),name='update-invoice'),
    path('delete/<int:id>/',views.DeleteInvoiceView.as_view(),name='delete-invoice'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)