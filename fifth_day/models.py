from django.db import models

class Product(models.Model):
    Product_Name=models.CharField(max_length=100,null=True)
    Product_Code=models.CharField(max_length=100,null=True)
    Product_Price=models.FloatField(default=0)
    Product_Gst=models.IntegerField(default=0)
    Food_Product=models.BooleanField(default=False)

    def __str__(self):
        return self.Product_Name