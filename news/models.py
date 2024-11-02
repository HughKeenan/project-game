from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    """
    Stores a thread post related to :model `auth.User`
    """
    title = models.CharField(max_length=150, unique = True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    poster = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="news_posts")
    body = models.TextField(blank=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-posted_on"]
    def __str__(self):
        return f"{self.title} - {self.poster}" 
          

class Response(models.Model):
    """
    Stores a reponse post related to :model `auth.Thread`
    """
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.RESTRICT, related_name="responses")
    content = models.TextField(blank=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    class Meta:
        ordering = ["posted_on"]
    def __str__(self):
        return f"{self.content} - {self.poster}"   
      