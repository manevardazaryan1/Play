from django.urls import path

from user import views

# user app urls.py

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/<str:user_name>', views.profile, name='profile'),
    path('add_my_playlist/<int:pk>', views.add_my_playlist, name='add_my_playlist'),
    path('my_playlist/<str:user_name>', views.my_playlist, name='my_playlist')
]
