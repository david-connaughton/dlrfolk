from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    artist = models.CharField(max_length=200, default="Artist")
    date_one = models.DateField()
    content = models.TextField(default="Content Goes Here")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_by = models.CharField(max_length=200, default="Shane Connaughton")
    artist_website = models.URLField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist

    class Meta:
        ordering = ['date_one']
