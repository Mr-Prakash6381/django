from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def Eighth(request):

    return render(request,'eighth.html')

def LoginPage(request):

    if request.method=='POST':

        print(request.POST)

        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)

        if user is not None:

            login(request,user)
            return redirect('eighth.html')
        else :
            
            sender={
                "error":"Invalid UserName or Password"
            }

            return render(request,'loginPage.html',sender)
        




    return render(request,'loginPage.html')

def LogoutUser(reuqest):
    logout(reuqest)
    return redirect('loginPage.html')
