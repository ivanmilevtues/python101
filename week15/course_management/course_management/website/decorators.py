from django.shortcuts import redirect


def annon_required(redirect_url):
    if not redirect_url:
        redirect_url = '/login'

    def take_func(func):
        def decorated(req, *args, **kwargs):
            if 'email' in req.session.keys():
                return func(req, *args, **kwargs)
            else:
                return redirect(redirect_url)
        return decorated
    return take_func


def login_required(redirect_url):
    if not redirect_url:
        redirect_url = '/'

    def take_func(func):
        def decorated(req, *args, **kwargs):
            if 'email' not in req.session.keys():
                return func(req, *args, **kwargs)
            else:
                return redirect(redirect_url)
        return decorated
    return take_func
