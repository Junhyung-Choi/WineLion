import csv
import os
import django
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTING_MODULE","hackathonProj.settings")
django.setup()

from hackathonApp.models import *



def insert_wine():
    CSV_PATH = "/Users/cho/Desktop/wine/WineLion/hackathonProj/data/winedata.csv"
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
    CSV_PATH = "/Users/cho/Desktop/wine/WineLion/hackathonProj/data/fooddata.csv"
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
    CSV_PATH = "/Users/cho/Desktop/wine/WineLion/hackathonProj/data/reviewdata.csv"
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

# insert_wine()
# insert_food()
# insert_review()



