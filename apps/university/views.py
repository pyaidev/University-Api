from django.shortcuts import render

from apps.blog.models import Blog
from apps.course.models import Course
from .models import About, FAQ, Reason, Service



def home_view(request):
    courses = Course.objects.all().order_by('-id')
    teachers = Ac.objects.filter(role=1).order_by('-id')[:3]
    posts = Blog.objects.order_by('-id')[:5]
    context = {
        'teachers': teachers,
        'courses': courses,
        'posts': posts,
    }

    return render(request, 'index.html', context)


def about(request):
    about = About.objects.all().order_by('-id')[:1]
    service = Service.objects.all().order_by('-id')
    faq = FAQ.objects.all()
    reason = Reason.objects.order_by('-id')
    context = {
        'abouts': about,
        'services': service,
        'reasons': reason,
        'faqs': faq
    }
    return render(request, 'about.html', context)