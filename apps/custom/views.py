from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import Custom



class UpdateCustomView(UpdateView):
    model = Custom
    fields = ['castom_bg']
    context_object_name = 'custom'
    success_url = reverse_lazy('index')
