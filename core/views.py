from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
        if receipt.user != request.user: # type: ignore
            return HttpResponseForbidden('You do not have the permission to access this receipt')
        
        return super().dispatch(request, *args, **kwargs)
