from django.contrib import admin

from .models import Comment, Music

# Register your models here.



admin.site.register(Music)
admin.site.register(Comment)