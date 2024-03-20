"""
URL configuration for invoiceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from InvoiceApp.serializerview import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Customer",CustomerView.as_view()),
     path("Product",ProductView.as_view()),
      path("Invoice",InvoiceView.as_view()),
       path("Payment",PaymentView.as_view()),
        path("Invoiceproduct",InvoiceproductView.as_view())
]
