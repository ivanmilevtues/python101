from django.shortcuts import render
from lecture.models import Lecture
# Create your views here.


def add_lecture(request):
    if request.method == 'POST':
        name = request.POST['name']
        week = request.POST['week']
        url = request.POST['url']
        Lecture.objects.create(name=name, week=week, url=url)
        object_added = True

    return render(request, "lecture_create_form.html", locals())
