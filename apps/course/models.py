from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


def path_to_course_image(instance, filename):
    category = instance.category.title
    course = instance.title
    return '{0}/{1}/images/{2}'.format(category, course, filename)


def path_to_lesson_video(instance, filename):
    category = instance.course.category.title
    course = instance.course.title
    lesson = instance.title
    return '{0}/{1}/{2}/videos/{3}'.format(category, course, lesson, filename)


class Course(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to=path_to_course_image)
    category = models.ForeignKey('blog.Category', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('blog.Tag', blank=True)
    description = RichTextField()
    detail = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    duration = models.CharField(max_length=21)
    video = models.FileField(upload_to=path_to_lesson_video)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


