from django.urls import path, include
from .views import CommentListCreateView

urlpatterns = [
    path('<int:pk>/list-create/', CommentListCreateView.as_view())
]