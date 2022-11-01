from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.course.api.v1.urls'))
]