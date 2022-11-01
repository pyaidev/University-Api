from django.urls import path
from .views import course_view, add_course, course_detail
app_name = 'course'

urlpatterns = [
    path('', course_view, name='list'),
    path('course/<int:pk>/', course_detail, name='detail'),
    path('add-course/', add_course, name='add_course'),
]
