from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from core import views



urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #path('register/', views.RegisterView.as_view(), name='auth_register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)