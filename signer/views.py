from django.db.models import Q
from django.views.generic import DetailView, ListView

from .forms import SignerSearchForm
from .models import Signer

# signer app view.py

class SignerView(ListView):
    """Signer view class"""

    model = Signer
    template_name = '../templates/signer/signer.html'
    context_object_name = 'signers'
    paginate_by = 16
    form_class = SignerSearchForm

    def get_queryset(self):
        """SignerView class get queryset function"""

        queryset = self.model.objects.all().order_by('-pk')

        if self.request.GET.get('search'):
            first_name = Q(first_name__icontains=self.request.GET.get('first_name', ''))
            last_name = Q(last_name__icontains=self.request.GET.get('last_name', ''))
            queryset = queryset.filter(first_name, last_name,)
            
        return queryset 

    def get_context_data(self, **kwargs):
        """SignerView class get context data function"""

        context = super(SignerView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context



class SignerDetailView(DetailView):
    """Signer detail view"""
    
    queryset = Signer.objects.all()
    template_name = '../templates/signer/detail.html'
    context_object_name = 'signer'
