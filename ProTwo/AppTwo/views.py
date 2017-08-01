from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # c = { 'dict_key': 'this is looking for help/index.html'}
    return HttpResponse('<em>My Second App</em>')
    # return render(request, 'help/index.html', context = c)

def help(request):
    help_dict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context=help_dict)

def login(request):
    login_dict = {'dict_key_login' : 'this is the login page!'}

    return render(request, 'AppTwo/login.html', context=login_dict)

def about(request):
    about_dict = {
        'about_us_dict_key' : 'this is cool stuff about us!'
    }
    return render(request, 'AppTwo/about.html', context=about_dict)
