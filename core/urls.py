from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import ReceiptListView, ReceiptDetailView, ReceiptUpdateView, ReceiptCreateView, ReceiptDeleteView

urlpatterns = [
    path('receipt', ReceiptListView.as_view(), name='receipt_list'),
    path('receipt/<int:pk>', ReceiptDetailView.as_view(), name='receipt_detail'),
    path('receipt/<int:pk>/edit', ReceiptUpdateView.as_view(), name='receipt_update'),
    path('receipt/<int:pk>/delete', ReceiptDeleteView.as_view(), name='receipt_delete'),
    path('receipt/create/', ReceiptCreateView.as_view(), name='receipt_create')    
]
