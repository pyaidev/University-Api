from django.urls import path
from .views import blog_view, blog_single

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<int:pk>/', blog_single, name='blog-single'),
]
