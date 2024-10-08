from django.shortcuts import render
from django.views import generic
from .models import Thread

# Create your views here.
class ThreadList(generic.ListView):
    queryset = Thread.objects.all()
    template_name = "thread_list.html"