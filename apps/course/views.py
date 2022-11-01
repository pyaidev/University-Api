from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

from apps.course.models import Course
from apps.profiles.models import MyCourse


def course_view(request):
    courses = Course.objects.all().order_by('-id')
    recent_courses = Course.objects.all()

    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    author = request.GET.get('author')
    date = request.GET.get('date')

    if cat:
        courses = courses.filter(category__title__exact=cat)

    if tag:
        courses = courses.filter(tags__title__exact=tag)

    if author:
        courses = courses.filter(author__account__username__exact=author)

    if date:
        courses = courses.filter(created_at__contains=date)
    my_course_id_list = []
    my_course_list = MyCourse.objects.filter(profile_id=request.user.profile.id)
    for i in my_course_list:
        my_course_id_list.append(i.course.id)

    context = {
        'posts': courses,
        'my_course_id_list': my_course_id_list,
        "recent_courses": recent_courses
    }

    return render(request, 'courses.html', context)


def course_detail(request, pk):
    course = Course.objects.get(id=pk)

    context = {
        "course": course,
    }
    return render(request, 'course-single.html', context)


@login_required
def add_course(request):
    cid = request.GET.get('_cid')
    profile_id = request.user.profile.id
    my_courses = MyCourse.objects.filter(profile_id=profile_id)
    data = {}
    my_course_id_list = []
    for i in my_courses:
        my_course_id_list.append(i.course.id)

    if int(cid) in my_course_id_list:
        print('if')
        MyCourse.objects.filter(course_id=cid).delete()
        data['message'] = 'Kurslar royhatidan ochirildi'
    else:
        print('else')
        MyCourse.objects.create(course_id=cid, profile_id=profile_id)
        data['message'] = 'Kurslar royhatiga qoshildi'

    return JsonResponse(data, status=200)
