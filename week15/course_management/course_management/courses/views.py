from django.shortcuts import render
from courses.models import Course

# Create your views here.


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
