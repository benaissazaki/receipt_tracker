from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import ReceiptListView, ReceiptDetailView, ReceiptUpdateView, ReceiptCreateView

urlpatterns = [
    path('receipt', login_required(ReceiptListView.as_view(),
         login_url=reverse_lazy('login')), name='receipt_list'),
    path('receipt/<int:pk>', login_required(ReceiptDetailView.as_view(),
         login_url=reverse_lazy('login')), name='receipt_detail'),
    path('receipt/<int:pk>/edit', login_required(ReceiptUpdateView.as_view(),
         login_url=reverse_lazy('login')), name='receipt_update'),
    path('receipt/create/', login_required(ReceiptCreateView.as_view(),
         login_url=reverse_lazy('login')), name='receipt_create')
    
]
