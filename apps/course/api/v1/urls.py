from django.urls import path
from .views import CourseListView, CourseCreateView, CourseRUDView, LessonGetListView, LessonPostListView

urlpatterns = [
    path('list/', CourseListView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('rud/<int:pk>/', CourseRUDView.as_view()),
    path('course/<int:course_id>/lessons/list/', LessonGetListView.as_view()),
    path('course/<int:course_id>/lessons/create/', LessonPostListView.as_view()),
]
