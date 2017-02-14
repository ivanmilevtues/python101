from django.shortcuts import render, redirect
from website.models import User
from website.decorators import annon_required, login_required
# Create your views here.


def register(req):
    if req.method == 'POST':
        first_name = req.POST['name'].split(' ')[0]
        last_name = req.POST['name'].split(' ')[1]
        User.objects.create(email=req.POST['email'], first_name=first_name,
                            last_name=last_name, password=req.POST['password'])
        return redirect(req, 'login.html', locals())
    return render(req, 'register.html', locals())


@login_required()
def login(req):
    if req.method == 'POST':
        email = req.POST['email']
        password = req.POST['password']
        user = User.objects.filter(email=email, password=password).first()
        if not user:
            error = 'invalid email or password.'
        else:
            error = 'You have logged in successfully'
            req.session['email'] = email
            return redirect('/profile')
    return render(req, 'login.html', locals())


@login_required()
def logout(req):
    try:
        del req.session['email']
    except KeyError:
        pass
    return redirect('/login')


@annon_required('/login')
def profile(req):
    if req.method == 'POST':
        return logout(req)
    user_information = User.objects.filter(email=req.session['email']).first()
    return render(req, 'profile.html', locals())
