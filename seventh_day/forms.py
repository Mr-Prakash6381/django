from django.forms import ModelForm
from .models import *

class Orders_Form(ModelForm):
    class Meta:
        model=Order
        fields=['Customer_reference','Product_reference','Order_number','Order_data','Quantity']