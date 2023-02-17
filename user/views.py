from django.urls import reverse, reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.views.generic import (CreateView)
from django.contrib.auth.views import LoginView, LogoutView

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