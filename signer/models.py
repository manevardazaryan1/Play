from django.db import models
from django.urls import reverse

# signer app models.py

def upload_image(instance, filename):
    """Upload images function"""

    return f'images/{instance.first_name}_{instance.last_name}/{filename}'

class Signer(models.Model):
    """Signer model class"""

    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to=upload_image, blank=True)


    def get_absolute_url(self):
        """Signer class meta class get absolute url function"""

        return reverse('signer:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """Signer class str function"""

        return f'{self.first_name} {self.last_name}'
    
    def Signer_list(self):
        """Signer class movies function"""
        
        return ''.join([i.name for i in self.music.all()])


    class Meta:
        """Signer class meta class"""

        verbose_name = 'Signer'
        verbose_name_plural = 'Signers'