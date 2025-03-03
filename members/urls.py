from django.urls import path
from .views import UserRegisterView
from .views import profile_view
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
]