from django.urls import path
from .views import *

urlpatterns=[
    path('',NinthDay.as_view())
]  