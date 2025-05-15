from django.urls import path
from .views import *

urlpatterns=[
    path('first/',Eighth),
    path('login/',LoginPage),
    path('logout/',LogoutUser)
]