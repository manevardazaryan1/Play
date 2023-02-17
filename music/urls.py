from django.urls import path

from music import views

# music app urls file

app_name = 'music'

urlpatterns = [
    path('music/', views.IndexView.as_view(), name='music'),
    path('music/detail/<int:pk>/', views.MusicDetailView.as_view(), name='detail'),
]


