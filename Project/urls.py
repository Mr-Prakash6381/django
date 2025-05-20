"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstday/',include('first_day.urls')),
    path('secondday/',include('second_day.urls')),
    path('threeday/',include('three_day.urls')),
    path('fourthday/',include('fourth_day.urls')),
    path('fifthday/',include('fifth_day.urls')),
    path('sixthday/',include('sixth_day.urls')),
    path('seventhday/',include('seventh_day.urls')),
    path('eigthday/',include('eighth_day.urls')),
    path('ninthday/',include('ninth_day.urls'))
]
