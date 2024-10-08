from django.shortcuts import render
from django.views import generic
from .models import Thread

# Create your views here.
class ThreadList(generic.ListView):
    """
    Displays all objects in the Threads model
    """
    queryset = Thread.objects.all()
    template_name = "thread_list.html"