from django.db.models import Q
from django.views.generic import DetailView, ListView

from .forms import SingerSearchForm
from .models import Singer

# singer app view.py

class SingerView(ListView):
    """Singer view class"""

    model = Singer
    template_name = '../templates/singer/singer.html'
    context_object_name = 'singers'
    paginate_by = 32
    form_class = SingerSearchForm

    def get_queryset(self):
        """SingerView class get queryset function"""

        queryset = super().get_queryset()

        if self.request.GET.get('search'):
            name = Q(name__icontains=self.request.GET.get('name', ''))
            queryset = queryset.filter(name)
            
        return queryset 

    def get_context_data(self, **kwargs):
        """SingerView class get context data function"""

        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context



class SingerDetailView(DetailView):
    """Singer detail view"""
    model = Singer
    template_name = '../templates/singer/detail.html'
    context_object_name = 'singer'
