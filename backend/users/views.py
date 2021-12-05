from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.template import loader

from users.forms import UserForm, UserDetailsForm


def home(request):
    template = loader.get_template("users/home.html")
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:details')

    else:
        form = UserForm(initial={'email': '@gmail.com'})

    return render(request, 'users/signup.html', {'form': form})


def details(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('users:home')

    else:
        form = UserDetailsForm(initial={'username': request.user.username,
                                        'email': request.user.email})

    return render(request, 'users/signup.html', {'form': form})
