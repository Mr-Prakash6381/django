from django.urls import path
from .views import *

urlpatterns=[
    path('basics/',Basics,),
    path('foter/',Footer,),
    path('nav/',Nav,),

]