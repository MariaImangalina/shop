from django.shortcuts import render
from .forms import CreateUser
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

class Signup(CreateView):
    form_class = CreateUser
    success_url = reverse_lazy('/')
    template_name = 'accounts/signup.html'


class UserPage(DetailView):
    model = get_user_model()

