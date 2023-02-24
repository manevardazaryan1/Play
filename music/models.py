from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from singer.models import Singer

from .helpers import upload_image

# music app models.py


class Music(models.Model):
    """Music model class"""

    name = models.CharField(max_length=155)
    genre = models.CharField(max_length=155)
    audio = models.TextField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_image, blank=True)
    is_published = models.BooleanField(default=True)
    singer = models.ManyToManyField(Singer, related_name='music')

    def __str__(self):
        """Music class str function"""

        return self.name

    class Meta:
        """Music class meta class"""

        verbose_name = "Music"
        verbose_name_plural = "Music"

    def get_absolute_url(self):
        """Music class meta class get absolute url function"""

        return reverse('music:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """Comments model"""
    
    music = models.ForeignKey(Music, related_name='music_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
