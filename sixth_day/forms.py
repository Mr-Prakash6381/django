from django.forms import ModelForm
from .models import *

class Student_Form(ModelForm):
    class Meta:
        model= Student
        fields= '__all__' 