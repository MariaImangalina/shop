from django.shortcuts import render
from django.views import generic
from .models import Good
from django.contrib.auth.mixins import LoginRequiredMixin 

class GoodsList(generic.ListView):
    model = Good

class GoodDetail(generic.DetailView):
    model = Good

class CreateGood(generic.CreateView, LoginRequiredMixin):
    model = Good
    fields = '__all__'

class GoodUpdate(generic.UpdateView, LoginRequiredMixin):
    model = Good
    fields = '__all__'