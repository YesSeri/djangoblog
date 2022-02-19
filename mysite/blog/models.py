from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.

from django.contrib.auth.models import User


DEFAULT_ID = 1


class Topic(models.Model):
    name = models.CharField(
        max_length=60, help_text="Enter a topic for your post, e.g. Javascript, Relationship", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        default=DEFAULT_ID,
    )
    topic = models.ManyToManyField(
        Topic, help_text="Select a topic for this post")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    class Meta:
        ordering = ('-created_date', )
