# invoices/admin.py
from django.contrib import admin
from .models import Invoice, InvoiceDetail

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'customer_name']

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'description', 'quantity', 'unit_price', 'price']
