from django.shortcuts import render
from django.views import generic
from .models import Good

class GoodsList(generic.ListView):
    model = Good

class GoodDetail(generic.DetailView):
    model = Good