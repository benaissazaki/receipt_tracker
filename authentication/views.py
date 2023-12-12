from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormView(FormView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())
