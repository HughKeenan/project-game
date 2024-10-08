from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Stores a thread post related to :model `auth.User`
"""
class Thread(models.Model):
    title = models.CharField(max_length=150, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    poster = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="news_posts")
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-posted_on"]
    def __str__(self):
        return f"{self.title} - {self.poster}"    

class Response(models.Model):
    """
    Stores a reponse post related to :model `auth.Thread`
    """
    thread = models.ForeignKey(Thread, on_delete=models.RESTRICT, related_name="responses")
    poster = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="responder")
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-posted_on"]
    def __str__(self):
        return f"{self.body} - {self.poster}"    