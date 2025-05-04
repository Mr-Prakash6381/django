from django.urls import path
from .views import *

urlpatterns=[
    path('',HomePage,name='first_day')
]