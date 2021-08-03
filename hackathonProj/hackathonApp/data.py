# ===================================================
# =              코드 수정 전에 주의사항!           =
# =              2021-08-03 09:52 기준              =
# =              CSV 기준으로 DB입력이 끝나서       =
# =              db.sqlite3 파일을 지우지 않는한    =
# =              아래 함수들을 사용하지 말 것!      =
# =                  - Junhyung-Choi -              =
# ===================================================

import csv
import os
import sys
import django
from django.utils import timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ.setdefault("DJANGO_SETTING_MODULE",'hackathonProj.settings')
django.setup()

from hackathonApp.models import *

def insert_wine():
    CSV_PATH = os.path.join(BASE_DIR,"../data/windedata.csv")
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            # print(row)
            Wine.objects.create(
                name = row['name'],
                kind = row['kind'],
                country = row['country'],
                price = row['price'],
                grape_type1 = row['grape_kind1'],
                grape_type2 = row['grape_kind1'],
                explain = row['explain'],
                taste1 = row['taste1'],
                taste2 = row['taste2'],	
                alchol = row['alchol'],
                dry = row['dry'],
                body = row['body'],
                tannin = row['tannin'],
            )
    print("와인 성공!")

def insert_food():
    CSV_PATH = os.path.join(BASE_DIR,"../data/fooddata.csv")
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            print(row)
            Food.objects.create(
                name = row['name'],
                location = row['type'],
                tag1 = row['tag1'],
                tag2 = row['tag2'],
            )
    print("음식 성공!")


def insert_review():
    
    CSV_PATH = os.path.join(BASE_DIR,"../data/reviewdata.csv")
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            print(row)
            Review.objects.create(
                referring_user_id_id = row['user_id'],
                write_time = row['write_time'],
                last_modified_time = row['write_time'],
                star = row['star'],
                body = row['body'],
                referring_wine_id_id = row['wine_id'],
            )
            
    print("리뷰 성공!")

def insert_wine2food():
    
    CSV_PATH = os.path.join(BASE_DIR,"../data/wine2fooddata.csv")
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            print(row)
            wine = Wine.objects.get(id=int(row['wine_id']))
            #음식 데이터셋 3번 넣고 지우니까 id 71 * 3개 밀려서 213 더해놨음 db.sqlite3 파일 삭제 후 다시 진행시 213 지울 것
            food = Food.objects.get(id=(int(row['food_id'])+213))
            food.wines.add(wine)
            food.save()
    print("음식와인연결 성공!")

# insert_wine()
# insert_food()
# insert_review()



