from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.
def home(request):
    return render(request, 'registration/home.html')


# used to show success_message
class CustomLoginView(SuccessMessageMixin, LoginView):
    # template_name='users/login.html not needed by default it will look for registration/login.html
    success_message = "You were successfully logged in"
    success_url = '/'
    # LOGIN_REDIRECT_URL Specified in settings
    # crispy forms will not work without bootstrap
    """def get_success_url(self):   # can be used instead of LOGIN_REDIRECT_URL In settings
        return '/'"""


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created succesfully for {username}')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='/user/login/')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {'u_form': u_form, 'p_form': p_form})


def error_404(request, exception):
    return render(request, 'registration/error_404.html')


def error_500(request):
    return render(request, 'registration/error_404.html')
