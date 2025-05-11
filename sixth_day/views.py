from django.shortcuts import render,redirect
from .forms import *
from .models import *


def Sixthday(request):
    sender={
        'student_from':Student_Form()
    }
    if request.method == 'POST':
        Student_form=Student_Form(request.POST)
        
        if Student_form . is_valid():
            Student_form.save()
    return render(request,'sixth.html',sender)

def View(request):
    sender={
        'all_student':Student.objects.all()
    }
    return render(request,'view.html',sender)

def DeleteStudent(request,item_id):
    select_Student=Student.objects.get(id=item_id)
    select_Student.delete()
    return redirect('/sixthday/view/')


def StudentUpdata(request):
    select_student=Student.objects.get(id=id)
    sender={
        'product_from':Student_Form(instance=select_student)
    }
    if request.method=='POST':
        student_from=Student_Form(request.POST,instance=select_student)

        if student_from.is_valid():
            student_from.save()
            return redirect('/sixthday/view/')
    return render(request,'sixth.html',sender)