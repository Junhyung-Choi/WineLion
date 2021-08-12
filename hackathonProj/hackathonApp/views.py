from hackathonApp.data import *
from django.shortcuts import redirect, render, reverse

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
    if len(review) == 0:
        review = "리뷰가 없습니다."
    context = {
        "wine": Wine.objects.get(id = id),
        "reviews": review,
        "pic": "/static/img/list/num"+str(id)+".jpg",
        "body": "/static/img/score/score"+str(body)+".png",
        "tannin": "/static/img/score/score"+str(tannin)+".png",
        "dry": "/static/img/score/score"+str(dry)+".png",
        "star": star,
        "star_percent": str(int(star/5*100)) + str('%'),
    }
    if request.method == "POST" :  
        new_data = Review()
        user = request.user
        wine = Wine.objects.get(id = id)
        new_data.referring_user_id = user
        new_data.star = int(request.POST['star'])
        new_data.body = request.POST['body']
        new_data.referring_wine_id = wine
        if (new_data.star == 0 or new_data.body == ""):
            context['message'] = "형식을 확인해주세요."
            return render(request, 'riview.html', context)
        new_data.save()
        return redirect('wine_info', wine.id)
        
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
        foods = Food.objects.filter(location=request.POST["location"])
        wines = [{} for _ in range(len(foods))]
        rows = []
        i = 0
        for i in range(1,len(foods)//3+1):
            row = {}
            row['num'] = i
            row['cards'] = [{} for _ in range(3)]
            for j in range(3):
                row['cards'][j]['num'] = (i-1) * 3 + j
                row['cards'][j]['food'] = foods[(i-1) * 3 + j]
                row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
                row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
            rows.append(row)
        row = {}
        row['num'] = i+1
        row['cards'] = [{} for _ in range(len(foods) - (len(foods)//3) * 3)]
        i += 1
        for j in range(len(foods) - (len(foods)//3) * 3):
            row['cards'][j]['num'] = (i-1) * 3 + j
            row['cards'][j]['food'] = foods[(i-1) * 3 + j]
            row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
            row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
        rows.append(row)
        context = {
            "foods": foods,
            "wines": wines,
            "rows": rows,
        }
        return render(request, 'recommend.html',context = context)
    else:
        foods = Food.objects.filter(location="KR")
        wines = [{} for _ in range(len(foods))]
        rows = []
        i = 0
        for i in range(1,len(foods)//3+1):
            row = {}
            row['num'] = i
            row['cards'] = [{} for _ in range(3)]
            for j in range(3):
                row['cards'][j]['num'] = (i-1) * 3 + j
                row['cards'][j]['food'] = foods[(i-1) * 3 + j]
                row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
                row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
            rows.append(row)
        row = {}
        row['num'] = i+1
        row['cards'] = [{} for _ in range(len(foods) - (len(foods)//3) * 3)]
        i += 1
        for j in range(len(foods) - (len(foods)//3) * 3):
            row['cards'][j]['num'] = (i-1) * 3 + j
            row['cards'][j]['food'] = foods[(i-1) * 3 + j]
            row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
            row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
        rows.append(row)
        context = {
            "foods": foods,
            "wines": wines,
            "rows": rows,
        }
        return render(request, 'recommend.html',context = context)

def practice(request):
    if request.method == "POST":
        foods = Food.objects.filter(location=request.POST["location"])
        wines = [{} for _ in range(len(foods))]
        rows = []
        i = 0
        for i in range(1,len(foods)//3+1):
            row = {}
            row['num'] = i
            row['cards'] = [{} for _ in range(3)]
            for j in range(3):
                row['cards'][j]['num'] = (i-1) * 3 + j
                row['cards'][j]['food'] = foods[(i-1) * 3 + j]
                row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
                row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
            rows.append(row)
        row = {}
        row['num'] = i+1
        row['cards'] = [{} for _ in range(len(foods) - (len(foods)//3) * 3)]
        i += 1
        for j in range(len(foods) - (len(foods)//3) * 3):
            row['cards'][j]['num'] = (i-1) * 3 + j
            row['cards'][j]['food'] = foods[(i-1) * 3 + j]
            row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
            row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
        rows.append(row)
        context = {
            "foods": foods,
            "wines": wines,
            "rows": rows,
        }
        return render(request, 'recommend.html',context = context)
    else:
        foods = Food.objects.filter(location="KR")
        wines = [{} for _ in range(len(foods))]
        rows = []
        i = 0
        for i in range(1,len(foods)//3+1):
            row = {}
            row['num'] = i
            row['cards'] = [{} for _ in range(3)]
            for j in range(3):
                row['cards'][j]['num'] = (i-1) * 3 + j
                row['cards'][j]['food'] = foods[(i-1) * 3 + j]
                row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
                row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
            rows.append(row)
        row = {}
        row['num'] = i+1
        row['cards'] = [{} for _ in range(len(foods) - (len(foods)//3) * 3)]
        i += 1
        for j in range(len(foods) - (len(foods)//3) * 3):
            row['cards'][j]['num'] = (i-1) * 3 + j
            row['cards'][j]['food'] = foods[(i-1) * 3 + j]
            row['cards'][j]["img"] = "/static/img/foods/food" + str(row['cards'][j]['food'].id) + ".png"
            row['cards'][j]['wines'] = foods[(i-1) * 3 + j].wines.all()
        rows.append(row)
        context = {
            "foods": foods,
            "wines": wines,
            "rows": rows,
        }
        return render(request, 'recommend.html',context = context)

def wine_list(request):
    message = ""
    isSearch = False
    if request.method == "POST":
        wines = Wine.objects.filter(country = request.POST['location'])
        print(request.POST)
        if (request.POST['winename'] != ""):
            name_list = []
            for wine in Wine.objects.all():
                name_list.append(wine.name)
            print(name_list)
            if (request.POST['winename'] in name_list):
                return redirect('wine_info',Wine.objects.get(name = request.POST['winename']).id)
            else:
                message = "검색하신 와인이 존재하지 않습니다"
    else:
        wines = Wine.objects.all()    
    cards = [{} for _ in range(len(wines))]
    for i in range(len(wines)):
        cards[i]['img'] = "/static/img/list/num" + str(wines[i].id) + ".jpg"
        cards[i]['data'] = wines[i]
    context = {
        "cards": cards,
        "message": message,
    }
    return render(request, 'wine_list.html',context = context)
    
def selling(request):
    return render(request,'selling.html')


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