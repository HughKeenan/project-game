from django.shortcuts import render
from .models import Report

# Create your views here.
def report_guide(request):
    """
    Renders the Report page
    """
    report = Report.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "report/report.html",
        {"report": report},
    )