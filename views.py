from django.contrib.auth import login, authenticate  # add to imports
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_page(request):
    form = LoginForm()
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
                return redirect('/')
            else:
                message = 'Login failed. Please check your credentials.'
    return render(request, 'customlogin/login.html', context={'form': form, 'message': message})