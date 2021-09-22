from django.http.response import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request,*args,**kwargs)
            else:
                return HttpResponse('You are not autherized to view this page')
        return wrapper_function
    return decorator

def admin_only(function_view):
    def wrapper_function(request,*args,**kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-home')
        elif group == 'admin':
            return function_view(request,*args,**kwargs)
    return wrapper_function
