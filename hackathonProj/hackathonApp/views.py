from hackathonApp.data import *
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.
def main(request):
    context = {
        "wines": Wine.objects.all(),
    }
    return render(request,'main.html',context)

def wine_info(request,id):
    context = {
        "wine": Wine.objects.get(id = id),
        "reviews": Review.objects.filter(referring_wine_id = id)
    }
    return render(request,'riview.html',context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request= request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username = username, password = password)
            if user is not None:
                login(request, user)
            return redirect("main")
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, "message" : "회원정보를 확인해주세요."})    
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("main")

def base(request):
    return render(request,'base.html')

def signup(request):
    if request.method == "POST": #1
        form = RegisterForm(request.POST)
    
        if form.is_valid(): #2
            new_user = form.save()
            # new_user = models.CustomUser.objects.create_user(**form.cleaned_data) #5
            login(request, new_user)
        
        return redirect('main')

    else: #3
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form}) #4

def mypage(request):
    return render(request,'member.html')

def food_recommend(request):
    return render(request, 'recommend.html')


# ===================================================
# =              코드 수정 전에 주의사항!           =
# =              2021-08-03 09:52 기준              =
# =              CSV 기준으로 DB입력이 끝나서       =
# =              db.sqlite3 파일을 지우지 않는한    =
# =              insert_data를 사용하지 말 것!      =
# =                  - Junhyung-Choi -              =
# ===================================================
def insert_data(request):
    #insert_wine()
    #insert_food()
    #insert_review()
    #insert_wine2food()
    #fix_WR()
    fix_Wine()
    return redirect('main')