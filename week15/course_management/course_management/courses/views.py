from django.shortcuts import render

from courses.models import Course
from courses.forms import EditCourseForm
from courses.forms2 import CreateCourseForm
from website.decorators import teacher_persmission
from lecture.models import Lecture


def show_courses(request):
    courses = Course.objects.all()
    return render(request, 'show_courses.html', locals())


@teacher_persmission
def add_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
        object_added = True
    form = CreateCourseForm()
    return render(request, 'create_form.html', locals())


def show_course(request, **params):
    course = Course.objects.filter(name=params['course_name']).first()
    lectures = Lecture.objects.filter(course=course)

    return render(request, 'show_course.html', locals())


@teacher_persmission
def edit_course(request, **params):
    course = Course.objects.filter(name=params['course_name']).first()
    lectures = Lecture.objects.filter(course=course)
    if request.method == 'GET':
        form = EditCourseForm()
        return render(request, 'edit_couse.html', locals())
    elif request.method == 'POST':
        form = EditCourseForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['course_name']:
                course.name = form.cleaned_data['course_name']
            if form.cleaned_data['description']:
                course.description = form.cleaned_data['description']
            if form.cleaned_data['start_date']:
                course.start_date = form.cleaned_data['start_date']
            if form.cleaned_data['end_date']:
                course.end_date = form.cleaned_data['end_date']
            course.save()
    return render(request, 'edit_couse.html', locals())
