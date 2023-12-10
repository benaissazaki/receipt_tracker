from typing import Any
from django import http
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import RegisterForm

class RegisterFormView(FormView):
  template_name = 'authentication/register.html'
  form_class = RegisterForm
  success_url = '/'
  
  def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    if self.request.user.is_authenticated:
      return redirect(self.get_success_url())   # Redirect to homepage if the user is authenticated
    return super().dispatch(request, *args, **kwargs)
  
  def form_valid(self, form: RegisterForm) -> HttpResponse:
    user = form.save()
    login(self.request, user)
    
    return redirect(self.get_success_url())
