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
    obj = Wine.objects.get(id = id)
    body = (int(obj.body)-1)//2 + 1
    tannin = (int(obj.tannin)-1)//2 + 1
    dry = (int(obj.dry)-1)//2 + 1
    review = Review.objects.filter(referring_wine_id = id)
    star = 0
    if len(review) != 0 :
        for i in review:
            star += i.star
        star = star/int(len(review))
    context = {
        "wine": Wine.objects.get(id = id),
        "reviews": review,
        "pic": "/static/img/list/num"+str(id)+".jpg",
        "body": "/static/img/score/score"+str(body)+".png",
        "tannin": "/static/img/score/score"+str(tannin)+".png",
        "dry": "/static/img/score/score"+str(dry)+".png",
        "star": star,
        "star_percent": str(int(star/5*100)) + str('%')
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
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): #2
            new_user = form.save()
            # new_user = models.CustomUser.objects.create_user(**form.cleaned_data) #5
            login(request, new_user)
            return redirect('main')
        else:
            form = RegisterForm()
            return render(request, 'signup.html', {'form': form, "message": "password"})    
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form}) #4

def mypage(request):
    return render(request,'member.html')

def food_recommend(request):
    if request.method == "POST":
        foods = Food.objects.filter(location=request.POST['location'])
        wines = [{} for _ in range(len(foods))]
        for i in range(len(foods)):
            wines[i]["name"] = foods[i].name
            wines[i]["wine_list"] = []
            for wine in foods[i].wines.all():
                wines[i]["wine_list"].append(wine)
        context = {
            "foods": Food.objects.filter(location=request.POST['location']),
            "wines": wines
        }
        return render(request, 'recommend.html',context = context)
    return render(request, 'recommend.html')

def practice(request):
    return render(request,'side.html')


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
    #fix_Wine()
    return redirect('main')