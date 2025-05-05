from django.shortcuts import render

def IndexPage(request):
    data={
        #Employee /  Student
        "Category":"Student",
        "Name":"Prakash",
        'Salare':20000,
        "Course":"M.Sc",
        "Specification":"Computer Science",
        "Number":[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'index.html',data)