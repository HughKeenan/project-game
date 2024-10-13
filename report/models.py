from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title