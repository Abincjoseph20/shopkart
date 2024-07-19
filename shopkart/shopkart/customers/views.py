from django.shortcuts import render,redirect
from django.contrib.auth.models import User #for registration purpuss
from django.contrib.auth import authenticate,login,logout #for login purpuss
from . models import Customer
from django.contrib import messages
# Create your views here.

def sign_out(request):
    logout(request)
    return render(request,'index.html')
def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

                #CREATE USER ACCOUNT
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer account
            customer = Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            succes_messages='user create succfuly' # redirection to success
            messages.success(request,succes_messages)
        except Exception as e:
            error_message = "duplicate user and invalid input"  # redirection to success
            messages.error(request,error_message)

            #login
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user',context)

    return render(request,'accounts.html')