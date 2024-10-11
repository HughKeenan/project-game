from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    """
    Stores a report post
    """
    thread_url = models.URLField(blank=False)
    reported_user = models.CharField(blank=False)
    reason_for_report = models.TextField(blank=False)
    reporter_username = models.CharField(blank=False)
    reporter_email = models.EmailField(blank=False)
    def __str__(self):
        return f"Reported User:{self.reported_user} - reported by {self.reporter_username}" 
