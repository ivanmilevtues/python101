
from django.shortcuts import render

from lecture.models import Lecture
from lecture.forms import EditLectureForm
from lecture.form2 import CreateLectureForm
from courses.models import Course
from website.decorators import teacher_persmission
# Create your views here.


@teacher_persmission
def add_lecture(req):
    if req.method == 'POST':
        form = CreateLectureForm(req.POST)
        if form.is_valid():
            course = Course.objects.filter(name=form.cleaned_data['course'])\
                                   .first()
            Lecture.objects.create(name=form.cleaned_data['name'],
                                   week=form.cleaned_data['week'],
                                   url=form.cleaned_data['url'],
                                   course=course)
            object_added = True
    form = CreateLectureForm()
    return render(req, "lecture_create_form.html", locals())


def show_lectures(request, **params):
    lecture = Lecture.objects.filter(id=int(params['lecture_id'])).first()
    return render(request, "show_lecutres.html", locals())


@teacher_persmission
def edit_lecture(request, **params):
    lecture = Lecture.objects.filter(id=int(params['lecture_id'])).first()
    if request.method == 'GET':
        form = EditLectureForm()
    elif request.method == 'POST':
        form = EditLectureForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['name']:
                lecture.name = form.cleaned_data['name']
            if form.cleaned_data['week']:
                lecture.week = form.cleaned_data['week']
            if form.cleaned_data['url']:
                lecture.url = form.cleaned_data['url']
            if form.cleaned_data['course']:
                lecture.course = Course.objects\
                    .filter(name=form.cleaned_data['course']).first()
            lecture.save()
    return render(request, "edit_lecture.html", locals())
