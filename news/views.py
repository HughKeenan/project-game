from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Thread

# Create your views here.
class ThreadList(generic.ListView):
    """
    Displays all objects in the Threads model
    """
    queryset = Thread.objects.all()
    template_name = "news/index.html"
    paginate_by = 1

def thread_detail(request, slug):
    """
    Display an individual :model:`news.Thread`.

    **Context**

    ``thread``
        An instance of :model:`news.Thread`.

    **Template:**

    :template:`news/thread_detail.html`
    """

    queryset = Thread.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "news/thread_detail.html",
        {"thread": thread},
    )