from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


class LogoutInterfaceView(LoginRequiredMixin, LogoutView):
    template_name = "home/logout.html"


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.now()}
