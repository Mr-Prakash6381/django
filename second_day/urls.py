from django.urls import path
from .views import *

urlpatterns=[
    path('',IndexPage,name='second_day')

]