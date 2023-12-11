from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Receipt

class ReceiptListView(ListView):
    model = Receipt
    paginate_by = 10
    context_object_name = 'receipts'

    def get_queryset(self) -> QuerySet[Receipt]:
        return Receipt.objects.filter(user=self.request.user).order_by('date_of_purchase')