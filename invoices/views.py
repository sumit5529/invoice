# invoices/views.py
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
