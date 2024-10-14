from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Thread
from .forms import ResponseForm

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

    queryset = Thread.objects.filter(visible=0)
    thread = get_object_or_404(queryset, slug=slug)
    responses = thread.responses.all().order_by("-posted_on")
    response_count = thread.responses.filter().count()
    if request.method == "POST":
        response_form = ResponseForm(data=request.POST)
        if response_form.is_valid():
            response = response_form.save(commit=False)
            response.poster = request.user
            response.thread = thread
            response.save()
            
    response_form = ResponseForm()

    return render(
        request,
        "news/thread_detail.html",
        {
            "thread": thread,
            "responses": responses,
            "response_count": response_count,
            "response_form": response_form,
            },
    )