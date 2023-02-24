from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView

from music.models import Music

from .tasks import fibon

# base app views.py

class IndexView(TemplateView):
    """Index view"""
    
    template_name = '../templates/base/index.html'


class PlayerView(ListView):
    """Player view"""

    model = Music
    template_name = '../templates/base/player.html'
    context_object_name = 'music'

class AboutView(TemplateView):
    """Abot view"""

    template_name = '../templates/base/about.html'

def change_site_content(request):
    fibon.apply_async(kwargs={'n': 10})
    return redirect("base:index")