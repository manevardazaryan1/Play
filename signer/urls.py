from django.urls import path

from signer import views

# signer app urls file

app_name = 'signer'

urlpatterns = [
    path('signer/', views.SignerView.as_view(), name='signer'),
    path('signer/detail/<int:pk>/', views.SignerDetailView.as_view(), name='detail'),
]
