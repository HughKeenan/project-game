"""models for report app"""
from django.db import models


class Report(models.Model):
    """
    Stores the guidelines on reporting users
    """
    title = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title


class ReportUser(models.Model):
    """
    Stores a report post on a specific user
    """
    thread_url = models.URLField(blank=False)
    user_being_reported = models.CharField(blank=False, max_length=250)
    reason_for_report = models.TextField(blank=False)
    reporters_email = models.EmailField(blank=False)
    examined = models.BooleanField(default=False)
