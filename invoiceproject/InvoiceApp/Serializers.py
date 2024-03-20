from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from InvoiceApp.models import Customermodel
from InvoiceApp.models import Productmodel
from InvoiceApp.models import Invoicemodel
from InvoiceApp.models import Paymentmodel
from InvoiceApp.models import Invoiceproductmodel

class InvoiceproductSerializer(serializers.ModelSerializer):
    Customer_Name=PrimaryKeyRelatedField(queryset=Customermodel.objects.all(),many=False)
    Product_name=PrimaryKeyRelatedField(queryset=Productmodel.objects.all(),many=False)
    Total_Amount=PrimaryKeyRelatedField(queryset=Invoicemodel.objects.all(),many=False)
    Payment_Date=PrimaryKeyRelatedField(queryset=Paymentmodel.objects.all(),many=False)
    class Meta:
        model=Invoiceproductmodel
        fields=("id","Customer_Name","Product_name","Quantity","Rate","GST","Total_Amount","Payment_Date")

class PaymentSerializer(serializers.ModelSerializer):
    Total_Amount=PrimaryKeyRelatedField(queryset=Invoicemodel.objects.all(),many=False)
    Quantity=InvoiceproductSerializer(many=True,read_only=True)
    class Meta:
        model=Paymentmodel
        fields=("id","Quantity","Total_Amount","Payment_Date","Payment_Amount","Payment_mode","Payment_description")

class InvoiceSerializer(serializers.ModelSerializer):
     Customer_Name=PrimaryKeyRelatedField(queryset=Customermodel.objects.all(),many=False)
     Quantity=InvoiceproductSerializer(many=True,read_only=True)
     Payment_Date=PaymentSerializer(many=True,read_only=True)
     class Meta:
         model=Invoicemodel
         fields=("id","Customer_Name","Quantity","Total_Amount","Invoice_Date","Payment_Date")

class ProductSerializer(serializers.ModelSerializer):
     Quantity=InvoiceproductSerializer(many=True,read_only=True)
     class Meta:
         model= Productmodel 
         fields=("id","Product_name","Quantity","Weight","Rate","Igst","Cgst")

class CustomerSerializer(serializers.ModelSerializer):
      Quantity=InvoiceproductSerializer(many=True,read_only=True)
      Total_Amount=InvoiceSerializer(many=True,read_only=True)
      class Meta:
          model=Customermodel
          fields=("id","Customer_Name","Email_Address","Mobile_Number","Local_Address","Quantity","Total_Amount")
