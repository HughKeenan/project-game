from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report
from .forms import ReportUserForm


# Create your views here.
@login_required()
def report_guide(request):
    """
    Renders the Report page
    """
    report = Report.objects.all().order_by('-updated_on').first()
    report_user = ReportUserForm()
    if request.method == "POST":
        report_user_form = ReportUserForm(data=request.POST)
        if report_user_form.is_valid():
            report_user_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Thank you for submitting a report.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error, could not submit report!')

    return render(
        request,
        "report/report.html",
        {"report": report,
            "report_user": report_user},
    )
