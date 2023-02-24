from django.urls import path

from singer import views

# singer app urls file

app_name = 'singer'

urlpatterns = [
    path('singer/', views.SingerView.as_view(), name='singer'),
    path('singer/detail/<int:pk>/', views.SingerDetailView.as_view(), name='detail'),
]
