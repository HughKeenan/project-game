from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Thread, Response
from .forms import ResponseForm

# Create your views here.
class ThreadList(generic.ListView):
    """
    Displays all objects in the Threads model
    """
    queryset = Thread.objects.all()
    template_name = "news/index.html"
    paginate_by = 5

def thread_detail(request, slug):
    """
    Display an individual :model:`news.Thread`.

    **Context**

    ``thread``
        An instance of :model:`news.Thread`.

    **Template:**

    :template:`news/thread_detail.html`
    """

    queryset = Thread.objects.all()
    thread = get_object_or_404(queryset, slug=slug)
    responses = thread.responses.filter(visible=True).order_by("posted_on")
    response_count = thread.responses.filter().count()
    if request.method == "POST":
        response_form = ResponseForm(data=request.POST)
        if response_form.is_valid():
            response = response_form.save(commit=False)
            response.poster = request.user
            response.thread = thread
            messages.add_message(request, messages.SUCCESS, 'Response posted!')
            response.save()
            return HttpResponseRedirect(reverse("thread_detail", args=[slug]))
            
     
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

def response_edit(request, slug, response_id):
    """
    view to edit responses
    """
    if request.method == "POST":

        queryset = Response.objects.filter(visible=True)
        thread = get_object_or_404(Thread, slug=slug)
        response = get_object_or_404(queryset, pk=response_id)
        response_form = ResponseForm(data=request.POST, instance=response)

        if response_form.is_valid() and response.poster == request.user:
            response = response_form.save(commit=False)
            response.thread = thread
            response.save()
            messages.add_message(request, messages.SUCCESS, 'Response updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating response!')

    return HttpResponseRedirect(reverse('thread_detail', args=[slug]))

def response_delete(request, slug, response_id):
    """
    view to delete responses
    """
    queryset = Response.objects.filter(visible=True)
    thread = get_object_or_404(Thread, slug=slug)
    response = get_object_or_404(queryset, pk=response_id)

    if response.poster == request.user:
        response.delete()
        messages.add_message(request, messages.SUCCESS, 'Response deleted!')
    else:
        messages.add_message(request, messages.ERROR, "You cannot delete others' responses!")

    return HttpResponseRedirect(reverse('thread_detail', args=[slug]))
