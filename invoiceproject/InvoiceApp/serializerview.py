from rest_framework import generics
from InvoiceApp.models import *
from InvoiceApp.Serializers import *
class CustomerView(generics.ListCreateAPIView):
    queryset=Customermodel.objects.all()
    serializer_class=CustomerSerializer
    
class ProductView(generics.ListCreateAPIView):
    queryset=Productmodel.objects.all()
    serializer_class=ProductSerializer

class InvoiceView(generics.ListCreateAPIView):
    queryset=Invoicemodel.objects.all()
    serializer_class=InvoiceSerializer

class PaymentView(generics.ListCreateAPIView):
    queryset=Paymentmodel.objects.all()
    serializer_class=PaymentSerializer

class InvoiceproductView(generics.ListCreateAPIView):
    queryset=Invoiceproductmodel.objects.all()
    serializer_class=InvoiceproductSerializer
    
