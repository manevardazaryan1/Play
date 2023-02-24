from django.urls import path

from .views import MusicDetail, MusicsList

# music api urls

urlpatterns = [
    path("v1/songs/", MusicsList.as_view(), name="all_songs"),
    path("v1/song/<int:pk>/", MusicDetail.as_view(), name="song_detail"),
]