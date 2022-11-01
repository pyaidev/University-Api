from django.urls import path
from .views import AccountRegisterView, LoginView, AccountRetrieveUpdateView

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('retrieve-update/<int:pk>/', AccountRetrieveUpdateView.as_view()),
]