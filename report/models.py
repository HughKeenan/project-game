from django.db import models

# Create your models here.
"""
Stores the guidelines on reporting users
"""
class Report(models.Model):
    title = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


"""
Stores a report post on a specific user
"""
class ReportUser(models.Model):
    thread_url = models.URLField(blank=False)
    user_being_reported = models.CharField(blank=False,max_length=250)
    reason_for_report = models.TextField(blank=False)
    reporters_email = models.EmailField(blank=False)
    examined = models.BooleanField(default=False)      