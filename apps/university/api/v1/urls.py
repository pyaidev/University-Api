from django.urls import path, include
from .views import ReasonViewSet, ServiceViewSet, AboutViewSet, FaqViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reasons', ReasonViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'about', AboutViewSet)
router.register(r'faq', FaqViewSet)


urlpatterns = [
    path('', include(router.urls))
]