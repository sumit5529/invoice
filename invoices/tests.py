# invoices/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2022-01-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_get_invoice_detail(self):
        response = self.client.get(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, InvoiceSerializer(self.invoice).data)
    def test_update_invoice(self):
        # New data to update the existing invoice
        updated_data = {'date': '2022-02-01', 'customer_name': 'Updated Customer'}

        # Make a PUT request to update the existing invoice
        response = self.client.put(f'/invoices/{self.invoice.id}/', updated_data, format='json')

        # Check if the response status code is 200 (OK) indicating a successful update
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the object from the database to get the latest data
        self.invoice.refresh_from_db()

        # Check if the invoice data has been updated correctly
        self.assertEqual(self.invoice.customer_name, 'Updated Customer')

        # Optional: Check if the response data matches the updated invoice data
        expected_data = InvoiceSerializer(self.invoice).data
        self.assertEqual(response.data, expected_data)
