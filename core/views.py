from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Receipt


class ReceiptListView(ListView):
    model = Receipt
    paginate_by = 10
    context_object_name = 'receipts'

    def get_queryset(self) -> QuerySet[Receipt]:
        return Receipt.objects.filter(user=self.request.user).order_by('date_of_purchase')


class ReceiptDetailView(DetailView):
    model = Receipt
    context_object_name = 'receipt'

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        receipt = self.get_object()
        if receipt.user != request.user:  # type: ignore
            return HttpResponseForbidden('You do not have the permission to access this receipt')

        return super().dispatch(request, *args, **kwargs)


class ReceiptUpdateView(UpdateView):
    model = Receipt
    fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']
    template_name_suffix = '_update'
    context_object_name = 'receipt'

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        receipt = self.get_object()
        if receipt.user != request.user:  # type: ignore
            return HttpResponseForbidden('You do not have the permission to edit this receipt')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy('receipt_detail', args=[self.get_object().pk])


class ReceiptCreateView(CreateView):
    model = Receipt
    fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']
    template_name_suffix = '_create'
    context_object_name = 'receipt'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('receipt_detail', args=[self.object.pk]) # type: ignore


class ReceiptDeleteView(DeleteView):
    model = Receipt
    template_name_suffix = '_delete'
    context_object_name = 'receipt'

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        receipt = self.get_object()
        if receipt.user != request.user:  # type: ignore
            return HttpResponseForbidden('You do not have the permission to delete this receipt')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy('receipt_list')
