from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Custom users app
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Same endpoint, new view
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/dog/', include('dogs.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/articles/', include('articles.urls')),  # Include the articles app URLs
    path('api/health-index/', include('health_index.urls')),
    path('api/health-records/', include('health_records.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # Redirect root to admin
]

# This is to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)