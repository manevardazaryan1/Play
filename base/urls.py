from django.urls import path

from base import views

# base app urls file

app_name = 'base'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
