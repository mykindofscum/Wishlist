from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView

class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ItemCreate(CreateView):
    model = Item
    fields = ['description', 'quantity']

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'


