from django.db import models
from fifth_day.models import *


class Customer(models.Model):
    Customer_name=models.CharField(max_length=50,null=True)
    Customer_since=models.DateField(null=True)

    def __str__(self):
        return self.Customer_name
    
    

class Order(models.Model):
    Customer_reference=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product_reference=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    Order_number=models.CharField(max_length=50,null=True)
    Order_data=models.DateField(null=True)
    Quantity=models.FloatField(default=0)
    Amount=models.FloatField(default=0)

    def __str__(self):
        return self.Order_number