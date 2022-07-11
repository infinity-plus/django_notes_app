from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.now()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/auth.html"
    login_url = "admin/"
