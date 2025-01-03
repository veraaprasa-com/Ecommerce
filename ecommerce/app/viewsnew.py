from .forms import EmailForm
from django.shortcuts import render, redirect  # type: ignore
from django.http import HttpResponse  # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm  # type: ignore
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib import messages  # type: ignore
from .forms import Identify
from django.contrib.auth.models import User  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.core.mail import send_mail  # type: ignore


def EmailView(request):
    send_mail('Verify the Email Address',
              'Your joining date:25/12/2024',
              'sdixitgowda@gmail.com',
              ['gowdayashas999@gmail.com'],
              fail_silently=True)
    return HttpResponse('Mail Sent')


def ComposeEmailView(request):
    fm = EmailForm()
    context = {
        'form': fm
    }
    if request.method == 'POST':
        fm = EmailForm(request.POST)
        if fm.is_valid():
            to = fm.cleaned_data['to']
            cc = fm.cleaned_data['cc']
            sub = fm.cleaned_data['sub']
            body = fm.cleaned_data['body']
            rec = [to]
            if cc:
                cc = cc.split(',')
                rec.extend(cc)
            send_mail(sub,
                      body,
                      'sdixitgowda@gmail.com',
                      rec,
                      fail_silently=True)
            return HttpResponse('MailSent')
    return render(request, 'email.html', context)


def createuser(request):
    fm = UserCreationForm()
    context = {
        'form': fm
    }
    if request.method == 'POST':
        fm = UserCreationForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'user account created successfully ')
            return redirect('login')
    return render(request, 'register.html', context)


def signin(request):
    fm = AuthenticationForm()
    context = {
        'form': fm
    }
    if request.method == 'POST':
        fm = AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'invalid username or password')
            if user:
                if user.is_authenticated:
                    login(request, user)
                    return redirect('home')
                    messages.success(
                        request, 'user account created successfully ')
    return render(request, 'login.html', context)


def home(request):
    return render(request, 'home.html')


def signout(request):

    logout(request)
    return redirect('login')


def sample(request):
    if request.method == 'POST':
        messages.add_message(request, messages.SUCCESS, 'sample message')
    return render(request, 'sample.html')


def success_message(request):
    messages.success(request, 'this is a success message')
    return redirect('sample')


def warning_message(request):
    messages.warning(request, 'this is a warning message')
    return redirect('sample')


def error_message(request):
    messages.error(request, 'this is a error message')
    return redirect('sample')


def info_message(request):
    messages.info(request, 'this is a info message')
    return redirect('sample')


@login_required(login_url='/signin/')  # type: ignore
def updatepassowrd(request, username):
    user = User.objects.get(username=username)
    fm = PasswordChangeForm(user)
    context = {
        'form': fm
    }
    if request.method == 'POST':
        fm = PasswordChangeForm(user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('password changed successfully')
        return HttpResponse('invalid password')
    return render(request, 'changepass.html', context)


def setpassword(request, username):
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        fm = SetPasswordForm(user)
        context = {
            'form': fm
        }
        if request.method == 'POST':
            fm = SetPasswordForm(user, data=request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponse('password changed successfully')
            return HttpResponse('invalid password')
        return render(request, 'setpassword.html', context)
    return HttpResponse('User does not exist')


def identifyView(request):
    fm = Identify()
    context = {
        'form': fm
    }
    if request.method == 'POST':
        fm = Identify(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            if User.objects.filter(username=uname).exists():
                url = '/resetpwd/'+uname+'/'
                return redirect(url)
            return redirect('signin')
        return render(request, 'identify.html', context)


def ResetPwd(request, uname):
    obj = User.objects.get(username=uname)
    fm = SetPasswordForm(obj)
    context = {
        'form': fm
    }
    if request.method == 'POST':
        fm = SetPasswordForm(obj, data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('signin')
    return render(request, 'resetpwd.html', context)