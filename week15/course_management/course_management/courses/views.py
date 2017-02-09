from django.shortcuts import render
from courses.models import Course
from lecture.models import Lecture


def show_courses(request):
    courses = Course.objects.all()
    return render(request, 'show_courses.html', locals())


def add_course(request):
    if request.method == "POST":
        name = request.POST["course_name"]
        description = request.POST["description"]
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        Course.objects.create(name=name, description=description,
                              start_date=start_date, end_date=end_date)
        object_added = True
    return render(request, 'create_form.html', locals())


def show_course(request, **params):
    course = Course.objects.filter(name=params['course_name']).first()
    lectures = Lecture.objects.filter(course=course)

    return render(request, 'show_course.html', locals())


def edit_course(request, **params):
    course = Course.objects.filter(name=params['course_name']).first()
    # Add lecture edit!!
    # use lecture.id as name to change but see what needs to be changed
    lectures = Lecture.objects.filter(course=course)
    if request.method == 'GET':
        return render(request, 'edit_couse.html', locals())
    elif request.method == 'POST':
        if request.POST['course_name']:
            course.name = request.POST['course_name']
        if request.POST['description']:
            course.description = request.POST['description']
        if request.POST['start_date']:
            course.start_date = request.POST['start_date']
        if request.POST['end_date']:
            course.end_date = request.POST['end_date']
    return render(request, 'edit_couse.html', locals())
