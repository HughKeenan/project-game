from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

VISIBLE = ((0, "Visible"), (1, "Invisible"))

# Create your models here.
"""
Stores a thread post related to :model `auth.User`
"""
class Thread(models.Model):
    title = models.CharField(max_length=150, unique = True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    poster = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="news_posts")
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    visible = models.IntegerField(choices=VISIBLE, default=0)
    class Meta:
        ordering = ["-posted_on"]
    def __str__(self):
        return f"{self.title} - {self.poster}" 

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()           

class Response(models.Model):
    """
    Stores a reponse post related to :model `auth.Thread`
    """
    poster = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="responder")
    thread = models.ForeignKey(Thread, on_delete=models.RESTRICT, related_name="responses")
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    visible = models.IntegerField(choices=VISIBLE, default=0)
    class Meta:
        ordering = ["posted_on"]
    def __str__(self):
        return f"{self.content} - {self.poster}"   


class NewThread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title         