from django.db import models
from django.urls import reverse

from signer.models import Signer

# music app models.py

def upload_image(instance, filename):
    """Upload images function"""

    return f'images/{instance.name}/{filename}'

def upload_audio(instance, filename):
    """Upload audio function"""

    return f'audio/{instance.name}/{filename}'


class Music(models.Model):
    """Music model class"""

    name = models.CharField(max_length=155)
    genre = models.CharField(max_length=155)
    lyrics = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to=upload_audio, blank=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_image, blank=True)
    is_published = models.BooleanField(default=True)
    signer = models.ManyToManyField(Signer, related_name='music')

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
