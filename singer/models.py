from django.db import models
from django.urls import reverse

from .helpers import upload_image

# singer app models.py


class Singer(models.Model):
    """Singer model class"""

    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to=upload_image, blank=True)


    def get_absolute_url(self):
        """Singer class meta class get absolute url function"""

        return reverse('singer:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """Singer class str function"""

        return f'{self.name}'
    
    def Singer_list(self):
        """Singer class singer function"""
        
        return ''.join([i.name for i in self.music.all()])
