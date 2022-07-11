import django
from django.shortcuts import redirect, render

# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):
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
    template_name = "home/login.html"


class LogoutInterfaceView(LoginRequiredMixin, LogoutView):
    template_name = "home/logout.html"


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.now()}
