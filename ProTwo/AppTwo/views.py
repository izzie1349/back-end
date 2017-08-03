from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo import forms

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

def users(request):
    users_list_ordered_by_email = User.objects.order_by('email')
    users_dict = {
        'users_key' : users_list_ordered_by_email,
    }
    return render(request, 'AppTwo/users.html', context=users_dict)

def user_form(request):
    form = forms.UserForm()

    # get user data
    if request.method == 'POST': # if someone hits submit and you get data back
        form = forms.UserForm(request.POST)
        if form.is_valid(): # check
            form.save(commit=True)
            return index(request)
        else:
            print('error form invalid')
    return render(request, 'AppTwo/user_form.html', { 'form':form })
