from django.shortcuts import render

def Basics(request):
    return render(request,'Basics.html')
def Footer(request):
    return render(request,'footer.html')
def Nav(request):
    return render(request,'nav.html')