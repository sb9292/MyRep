from django.db import models

# Create your models here.
class Customermodel(models.Model):
    Customer_Name=models.CharField(max_length=100)
    Email_Address=models.CharField(max_length=100)
    Mobile_Number=models.IntegerField()
    Local_Address=models.CharField(max_length=100)
    class Meta:
        db_table="tblcustomer"
        ordering=("Customer_Name",)
    def __str__(self):
        return  self.Customer_Name

class Productmodel(models.Model):
    Product_name=models.CharField(max_length=100)
    Weight=models.IntegerField()
    Rate=models.IntegerField()
    Igst=models.IntegerField()
    Cgst=models.IntegerField()
    class Meta:
        db_table="tblproduct"
        ordering=("Product_name",)
    def __str__(self):
        return self.Product_name   

class Invoicemodel(models.Model):
    Invoice_Date=models.CharField(max_length=100)
    Customer_Name=models.ForeignKey(Customermodel,related_name="Invoice",on_delete=models.CASCADE)
    Total_Amount=models.FloatField()
    class Meta:
        db_table="tblinvoice"
        ordering=("Total_Amount",)
    def __str__(self):
        return str(self.Total_Amount)    
    
class Paymentmodel(models.Model):
    Total_Amount=models.ForeignKey(Invoicemodel,related_name="payment",on_delete=models.CASCADE)
    Payment_Date=models.CharField(max_length=100)
    Payment_Amount=models.IntegerField()
    Payment_mode=models.CharField(max_length=100)
    Payment_description=models.CharField(max_length=100)
    class Meta:
        db_table="tblpayment"
        ordering=("Payment_Date",)
    def __str__(self):
        return str(self.Payment_Date)  

class Invoiceproductmodel(models.Model):
    Customer_Name=models.ForeignKey(Customermodel,related_name="product",on_delete=models.CASCADE)
    Product_name=models.ForeignKey(Productmodel,related_name="product",on_delete=models.CASCADE)
    Rate=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    GST=models.IntegerField()
    Total_Amount=models.ForeignKey(Invoicemodel,related_name="product",on_delete=models.CASCADE)
    Payment_Date=models.ForeignKey(Paymentmodel,related_name="product",on_delete=models.CASCADE)
    class Meta:
        db_table="tblinvoiceproduct"
        ordering=("Quantity",)
    def __str__(self):
        return str(self.Quantity)    