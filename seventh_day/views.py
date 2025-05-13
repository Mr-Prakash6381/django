from django.shortcuts import render
from .forms import *

def SevethDay(request):
    context={
        'Order_from':Orders_Form()
    }
    if request.method=='POST':
        select_product=Product.objects.get(id=request.POST['Product_reference'])
        Product_amount=float(select_product.Product_Price) * float(request.POST['Quantity'])
        get_amount=(select_product.Product_Gst) / 100
        bill_amount=Product_amount+get_amount

        new_Order=Order(Customer_reference_id=request.POST['Customer_reference'],
                    Product_reference_id=request.POST['Product_reference'],
                     Order_number=request.POST['Order_number'],
                      Order_data=request.POST['Order_data'],
                      Quantity=request.POST['Quantity'],
                      amount=Product_amount,
                      get_amount=get_amount,
                      bill_amount=bill_amount)
        new_Order.save()
    return render(request,'seventh.html',context)