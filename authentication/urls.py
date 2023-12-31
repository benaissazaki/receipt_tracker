from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreationFormView

urlpatterns = [
  path('register', UserCreationFormView.as_view(), name='register'),
  path('login', LoginView.as_view(template_name='authentication/login.html'), name='login'),
  path('logout', LogoutView.as_view(), name='logout'),
]
