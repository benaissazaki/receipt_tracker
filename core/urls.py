from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required

from core.views import ReceiptListView, ReceiptDetailView

urlpatterns = [
    path('receipt', login_required(ReceiptListView.as_view(),
         login_url=reverse_lazy('login')), name='receipt_list'),
    path('receipt/<int:pk>', login_required(ReceiptDetailView.as_view(),
         login_url=reverse_lazy('login')), name='receipt_detail')
]
