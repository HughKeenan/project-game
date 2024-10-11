from django.shortcuts import render
from .models import Report


def report_user(request):
    """
    Renders the Report page
    """
    report = Report.objects.all()

    return render(
        request,
        "report/report.html",
        {"report": report},
    )