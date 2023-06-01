from django.contrib.auth import login, authenticate  # add to imports
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_page(request):
    """
    This view takes GET parameter named "next" as input and redirect user to the request page if login form is submitted sucessfully
    """
    form = LoginForm()
    next_page = request.GET.get('next', '/')
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

    return render(request, 'customlogin/login.html', context={'form': form, 'message': message})