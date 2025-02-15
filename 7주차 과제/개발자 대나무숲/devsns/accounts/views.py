from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request) :
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def signin(request) :
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordcheck']:
            #회원가입
            new_user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
            #로그인
            auth.login(request, new_user)
            #홈으로 돌아가기
            return redirect('home')
        #비밀번호 확인이 틀렸을 때
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
# Create your views here.
