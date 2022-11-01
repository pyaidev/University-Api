from django.urls import path
from .views import home_view, about

app_name = 'university'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about)
]
