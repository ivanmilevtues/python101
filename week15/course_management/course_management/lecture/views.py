
from django.shortcuts import render
from lecture.models import Lecture
from courses.models import Course
# Create your views here.


def add_lecture(req):
    if req.method == 'POST':
        name = req.POST['name']
        week = req.POST['week']
        url = req.POST['url']
        course = Course.objects.filter(name=req.POST['course']).first()
        Lecture.objects.create(name=name, week=week, url=url, course=course)
        object_added = True

    return render(req, "lecture_create_form.html", locals())


def show_lectures(request, **params):
    lecture = Lecture.objects.filter(id=int(params['lecture_id'])).first()
    return render(request, "show_lecutres.html", locals())


def edit_lecture(request, **params):
    lecture = Lecture.objects.filter(id=int(params['lecture_id'])).first()
    if request.method == 'GET':
        print(lecture)
        return render(request, "edit_lecture.html", locals())
    elif request.method == 'POST':
        if request.POST['name']:
            lecture.name = request.POST['name']
        if request.POST['week']:
            lecture.week = request.POST['week']
        if request.POST['url']:
            lecture.url = request.POST['url']
        if request.POST['course']:
            lecture.course = Course.objects\
                .filter(name=request.POST['course']).first()
        lecture.save()
    return render(request, "edit_lecture.html", locals())
