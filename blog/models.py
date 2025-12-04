from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 # Import models to connect

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, default="Untitled Post")
    slug = models.SlugField(max_length=200, unique=True, default="Untitled Post")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", default=1)
    content = models.TextField(default="No content provided")
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True, default="")
    updated_on = models.DateTimeField(default=timezone.now)