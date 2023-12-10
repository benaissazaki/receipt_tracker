from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterFormView

urlpatterns = [
  path('register', RegisterFormView.as_view(), name='register'),
  path('login', LoginView.as_view(template_name='authentication/login.html'), name='login'),
  path('logout', LogoutView.as_view(), name='logout'),
]
