from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import RegisterForm


class RegisterFormView(FormView):
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = '/'

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.request.user.is_authenticated:
            # Redirect to homepage if the user is authenticated
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())
