from functools import wraps

from django.shortcuts import redirect
from django.http import HttpResponse

from website.models import Teacher


def annon_required(redirect_url):
    if not redirect_url:
        redirect_url = '/login'

    def take_func(func):
        @wraps(func)
        def decorated(req, *args, **kwargs):
            if 'email' in req.session.keys():
                return func(req, *args, **kwargs)
            else:
                return redirect(redirect_url)
        return decorated
    return take_func


def teacher_persmission(func):
    def check_for_permission(req, *args, **kwargs):
        if Teacher.objects.filter(email=req.session['email']).first():
            return func(req, *args, **kwargs)
        else:
            return HttpResponse(status=403)
    return check_for_permission


def login_required(redirect_url):
    if not redirect_url:
        redirect_url = '/'

    def take_func(func):
        @wraps(func)
        def decorated(req, *args, **kwargs):
            if 'email' not in req.session.keys():
                return func(req, *args, **kwargs)
            else:
                return redirect(redirect_url)
        return decorated
    return take_func
