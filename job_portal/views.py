from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method =='GET':
        context={
            'form': UserCreationForm(),
        }
        return render(request,'signup.html',context)
    else:
        user=UserCreationForm(request.POST)
        user.save()

        return redirect('signup')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user),
            return redirect('dashboard')
        else:
            return redirect('signin')





@login_required(login_url='/signin')
def dashboard(request):
    return render(request,'dashboard.html')

def my_logout(request):
        logout(request)
        return redirect('signin')

