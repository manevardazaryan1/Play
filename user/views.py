import json

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from music.models import Music

from .forms import RegisterForm

# User app view.py

class SuccessUrlMixin:
    """Success mixin class"""

    def get_success_url(self):
        return reverse("base:index")

class RegisterView(CreateView):
    """Register class"""

    model = User
    form_class = RegisterForm
    template_name = "user/register.html"
    success_url = reverse_lazy("user:login")

class LoginView(SuccessUrlMixin, LoginView):
    """Login class"""

    template_name = "user/login.html"


class Logout(LogoutView):
    """Log out class"""
    
    next_page = "base:index"

def profile(request,user_name):
    """Profile function"""

    if user_name != request.user.username:
        return redirect('base:index')
    user = User.objects.get(username=request.user.username)
    return render(request, 'user/profile.html', {'user': user})

def add_my_playlist(request,pk):
    music = Music.objects.get(pk=pk)
    music_pk = bool(request.user.profile.my_playlist.filter(pk=pk))

    if not music_pk:
        request.user.profile.my_playlist.add(music)

    return render(request, 'user/my_playlist.html')

def my_playlist(request,user_name):
    if user_name != request.user.username:
        return redirect('base:index')
    return render(request, 'user/my_playlist.html')