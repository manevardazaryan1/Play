import datetime

from django.db.models import Q
from django.views.generic import DetailView, ListView

from music.models import Music

from .forms import MusicSearchForm


class IndexView(ListView):
    """Music view class"""

    model = Music
    template_name = '../templates/music/music.html'
    paginate_by = 20
    context_object_name = 'music'
    form_class = MusicSearchForm

    def get_queryset(self):
        """IndexView class get queryset function"""

        queryset = self.model.objects.all().order_by('-pk')

        if self.request.GET.get('search'):
            name = Q(name__icontains=self.request.GET.get('name', ''))
            ganre = Q(genre__icontains=self.request.GET.get('genre', ''))
            queryset = queryset.filter(name, ganre)
        
        return queryset 

    def get_context_data(self, **kwargs):
        """IndexView class get context data function"""

        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

class MusicDetailView(DetailView):
    """Music detail view"""

    queryset = Music.objects.all()
    template_name = '../templates/music/detail.html'
    context_object_name = 'music'
