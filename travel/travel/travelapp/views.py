from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .email_utils import send_signup_email
def home(request):
    return render(request,'index2.html')
def index(request, page):
    template_name = f'{page}.html'
    return render(request, template_name)
def india(request, page):
    template_name = f'{page}.html'
    return render(request, template_name)
def booked(request):
    return render(request,'booked.html')
def tryy(request):
    return render(request,'try.html')
def form(request):
    return render(request,'form.html')
def registerr(request):
    if request.method=='POST': 
        uname=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        user_email = email  # Replace with the actual user's email
        send_signup_email(user_email)
        if password!=repassword:
            return HttpResponse("fbr9u")
        return redirect('login')

    return render(request,'register.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/index2/',{'user':user})
        else:
            return HttpResponse("username incorrect")
    return render (request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('/index2/')