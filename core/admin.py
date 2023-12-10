from django.contrib import admin
from .models import Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user', 'date_of_purchase', 'total_amount')
    list_filter = ('store_name', 'date_of_purchase')
