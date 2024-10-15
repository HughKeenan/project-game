from django.db import models
from django.contrib.auth.models import User

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

class Response(models.Model):
    """
    Stores a reponse post related to :model `auth.Thread`
    """
    poster = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="responder")
    thread = models.ForeignKey(Thread, on_delete=models.RESTRICT, related_name="responses")
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    visible = models.IntegerField(choices=VISIBLE, default=0)
    class Meta:
        ordering = ["-posted_on"]
    def __str__(self):
        return f"{self.body} - {self.poster}"   


class NewThread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title         