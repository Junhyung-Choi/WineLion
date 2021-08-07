from hackathonApp.data import *
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
    return render(request,'wine_info.html',context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request= request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username= username, password = password)
            if user is not None:
                login(request, user)
            return redirect("main")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("main")



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
    return redirect('main')


