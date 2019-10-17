from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('apps.core.urls')),
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token-refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
