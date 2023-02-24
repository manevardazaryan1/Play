from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField

from music.models import Music

from .helpers import upload_user_profile__image

# Create your models here.

class Profile(models.Model):
    """Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_user_profile__image, blank=True)
    my_playlist = models.ManyToManyField(Music, blank=True, null=True)

    def __str__(self):
        return self.user.username



# Profile creating after user registration 

@receiver(post_save, sender=User)
def send_profile_signal(sender, created, instance, **kwargs):
    """Profile creation function"""

    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
