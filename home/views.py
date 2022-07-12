from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class SignupView(CreateView):
    """Signup view to handle signing up a new user"""

    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "home/signup.html"

    def get(self, request, *args, **kwargs):
        return (
            redirect("list_notes")
            if request.user.is_authenticated
            else super().get(request, *args, **kwargs)
        )


class LoginInterfaceView(LoginView):
    """Login view to handle logging in a user"""

    template_name = "home/login.html"


class LogoutInterfaceView(LoginRequiredMixin, LogoutView):
    """Logout view to handle logging out a user"""

    template_name = "home/logout.html"


class HomeView(TemplateView):
    """Home view to handle the home page"""

    template_name = "home/welcome.html"
    extra_context = {"today": datetime.now()}
