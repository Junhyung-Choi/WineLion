from hackathonApp.data import *
from django.shortcuts import redirect, render

# Create your views here.
def main(request):
    context = {
        "wine":Wine.objects.get(id = 1),
        "food":Food.objects.get_queryset()[0].id
    }
    return render(request,'practice.html',context)

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


