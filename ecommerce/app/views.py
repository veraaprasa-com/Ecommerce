from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import (AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm)
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import Settings
# Create your views here.

def RegisrerView(request):
    fm=UserForm()
    context={
        'form':fm
    }
    if request.method=='POST':
        fm=UserForm(data=request.POST)
        if fm.is_valid():
            pswd1=fm.cleaned_data['password1']
            pswd2=fm.cleaned_data['password2']
            username=fm.cleaned_data['username']
            email=fm.cleaned_data['email']
            user_data_has_error=False
            if User.objects.filter(username=username).exists():
                user_data_has_error=True
                messages.error(request,'Username already exist')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                user_data_has_error=True
                messages.error(request,'Email already exist')
                return redirect('register')

            if user_data_has_error:
                return redirect('register')
            
            else:  
                if pswd1==pswd2:
                    fm.save()
                    messages.success(request,'User registration Successful')
                    return redirect('login')
                messages.error(request,'Both password are not matched')
    return render(request,'register.html',context)

def LoginView(request):
    fm=AuthenticationForm()
    context={
        'form':fm
    }
    if request.method=='POST':
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                if user.is_authenticated:
                    login(request,user)
                    messages.success(request,'user loggedin successfull')
                    return redirect('homepage')
                messages.error(request,'invalid username or password')
            return redirect('login')
    return render(request,'login.html',context)

def Logout_view(request):
    logout(request)
    messages.success(request,'User logged out successful')
    return redirect('login')

def Message_View(request):
    return render(request,'message.html')
@login_required
def Homepage(request):
    return render(request,'home.html')

def UpdatePassword(request,username):
    user=User.objects.get(username=username)
    fm=PasswordChangeForm(user)
    context={
        'form':fm
    }
    if request.method =='POST':
        fm=PasswordChangeForm(user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Password Updated successfully')
            return redirect('login')
        return HttpResponse('invalid password')
    return render(request,'update_password.html',context)

def ProductDataView(request):
    fm=product_item.objects.all()
    context={
        'productdata':fm
    }
    return render(request,'products/product_data.html',context)


def SingelProductItem(request,slug):
    if product_item.objects.filter(slug=slug).exists():
        product=product_item.objects.get(slug=slug)
        context={
            'product':product
        }
        return render(request,'products/single_product_item.html',context)
    return HttpResponse('product does not exist')

def CategoryView(request,slug):
    if product_category.objects.filter(slug=slug).exists():
        category=product_category.objects.get(slug=slug)
        products=product.objects.filter(product_category__exact=category)
        product_items=product_item.objects.filter(product__in=products)
        context={
            'product_items':product_items
        }
        return render(request,'products/categoryview.html',context)
    return HttpResponse('invalid category')

def Categories(request):
    categories=product_category.objects.filter(category_name__in=['Formal Shirts','Tshirt','Casual Shirts'])
    context={
        'categories':categories
    }
    return render(request,'categories.html',context)

def CartDisplay(request):
    items=OrderItemModel.objects.all()
    context={
        'items':items
    }
    return render(request,'cartdisplay.html',context)
def index(request):
    return render(request,'index.html')