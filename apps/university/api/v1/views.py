from ...models import Service, About, FAQ, Reason
from rest_framework import viewsets
from .serializers import UniversitySerializer


class ReasonViewSet(viewsets.ModelViewSet):
    # http: // 127.0.0.1:8000/api/university/v1/reasons/<id>
    queryset = Reason.objects.all()
    serializer_class = UniversitySerializer

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(Reason)
        return serializer


class ServiceViewSet(viewsets.ModelViewSet):
    # http: // 127.0.0.1:8000/api/university/v1/services/<id>
    queryset = Service.objects.all()
    serializer_class = UniversitySerializer

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(Service)
        return serializer

class AboutViewSet(viewsets.ModelViewSet):
    # http: // 127.0.0.1:8000/api/university/v1/about/<id>
    queryset = About.objects.all()
    serializer_class = UniversitySerializer

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(About)
        return serializer


class FaqViewSet(viewsets.ModelViewSet):
    # http: // 127.0.0.1:8000/api/university/v1/faq/<id>
    queryset = FAQ.objects.all()
    serializer_class = UniversitySerializer

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(FAQ)
        return serializer