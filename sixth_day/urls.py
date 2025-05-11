from django.urls import path
from .views import *

urlpatterns=[
    path('adddata/',Sixthday),
    path('view/',View),
    path('item/delect/<int:id>/',DeleteStudent,name='delete_item'),
    path('item/update/<int:id>/',StudentUpdata,name='update_item')
] 