from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=150, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_posts")
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)