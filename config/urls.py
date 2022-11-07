"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="University API Docs",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # SWAGGER
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ADMIN
    path('admin/', admin.site.urls),
    # MVT Pattern
    # path('t/', include('apps.university.urls', namespace='university')),
    # path('blog/', include('apps.blog.urls', namespace='blog')),
    # path('comment/', include('apps.comment.urls', namespace='comment')),
    # path('courses/', include('apps.course.urls', namespace='course')),
    # path('contact/', include('apps.contact.urls', namespace='contact')),
    # path('auth/', include('apps.accounts.urls', namespace='account')),
    # DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/accounts/', include('apps.accounts.api.urls')),
    path('api/blog/', include('apps.blog.api.urls')),
    path('api/comment/', include('apps.comment.api.urls')),
    path('api/contact/', include('apps.contact.api.urls')),
    path('api/course/', include('apps.course.api.urls')),
    path('api/university/', include('apps.university.api.urls')),
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
