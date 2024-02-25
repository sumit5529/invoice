# invoices/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoices')
# it will adjust url by itself
urlpatterns = [
    path('', include(router.urls)),
]
