from django.urls import path

from base import views

# base app urls file

app_name = 'base'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('change_content/', views.change_site_content, name="chnage_content"),
    path('player',views.PlayerView.as_view(), name='player'),
    path('about/',views.AboutView.as_view(), name='about')
]
