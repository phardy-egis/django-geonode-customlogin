from django.contrib.auth import login, authenticate  # add to imports
from django.shortcuts import render, redirect
from .forms import LoginForm
from urllib.parse import unquote_plus
from geonode.themes.context_processors import custom_theme
from django.urls import reverse
from .models import App

def login_page(request):
    """
    This view takes GET parameter named "next" as input and redirect user to the request page if login form is submitted sucessfully
    """
    form = LoginForm()
    next_page = unquote_plus(request.get_full_path().split("/?next=",1)[1])
    if not next_page:
        next_page = reverse("appselect")
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect(next_page)
            else:
                message = 'Login failed. Your account is disabled or your credentials are wrong.'
    else:
        if request.user.is_authenticated:
            return redirect(next_page)

    theme = custom_theme(request)

    try:
        logo_url = theme['custom_theme'].logo.url
        if not logo_url:
            logo_url = '/static/mapstore/img/geonode-logo.svg'
        title = theme['custom_theme'].name
        if not title:
            title = "Geonode"
    except :
        title = "Geonode"
        logo_url = '/static/mapstore/img/geonode-logo.svg'

    return render(request, 'customlogin/login.html', context={'form': form, 'message': message, 'logo': logo_url, 'title':title})

def app_selection_page(request):
    apps = App.objects.all()
    return render(request, 'customlogin/app_selection.html', context={'apps': apps})