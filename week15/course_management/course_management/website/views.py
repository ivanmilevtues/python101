from website.forms import PromoteUser, LoginForm
from website.forms2 import RegisterForm
from django.shortcuts import render, redirect, reverse
from website.models import User, Student, Teacher
from courses.models import Course
from website.decorators import annon_required, login_required
# Create your views here.


@login_required('/profile')
def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            if not User.exists(email=form.data['email']):
                form.save()
                return redirect(reverse('login'))
    form = RegisterForm()
    return render(req, 'register.html', locals())


@login_required('/profile')
def login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email'],
                                       password=form.cleaned_data['password'])\
                               .first()
            if not user:
                error = 'invalid email or password.'
            else:
                error = 'You have logged in successfully'
                req.session['email'] = form.cleaned_data['email']
                return redirect('/profile')
    form = LoginForm()
    return render(req, 'login.html', locals())


def logout(req):
    try:
        del req.session['email']
    except KeyError:
        pass
    return redirect('/login')


@annon_required('/login')
def profile(req):
    msg = "You are logged in"
    if req.method == 'POST':
        return logout(req)
    user_information = User.objects.filter(email=req.session['email']).first()
    if Teacher.objects.filter(email=req.session['email']).first():
        msg += ' as teacher.'
    elif Student.objects.filter(email=req.session['email']).first():
        msg += ' as student.'
    else:
        msg += ' as user.'
    return render(req, 'profile.html', locals())


def promote_user(req):
    if req.method == 'POST':
        form = PromoteUser(req.POST)
        if form.is_valid():
            try:
                user = User.objects.filter(email=form.cleaned_data['email'])\
                                   .first()
                course = Course.objects\
                               .filter(name=form.cleaned_data['course'])\
                               .first()
            except:
                error = 'Wrong email.'
                return render(req, 'promote_user.html', locals())

            promote_to = req.POST['promote_to']
            if promote_to == 'Teacher':
                Teacher.objects.create(first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.email, course=course,
                                       password=user.password)
                error = 'Successfully promted user to teacher.'
            elif promote_to == 'Student':
                Student.objects.create(first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.email, course=course,
                                       password=user.password)
                error = 'Successfully promted user to student.'
            else:
                error = 'No such promotion position'
    form = PromoteUser()
    return render(req, 'promote_user.html', locals())
