from django.views.generic import TemplateView

# base app views.py

class IndexView(TemplateView):
    template_name = '../templates/base/index.html'