from hackathonApp.data import *
from django.shortcuts import redirect, render

# Create your views here.
def main(request):
    # context = {"wine_data" : insert_wine()}
    return render(request,'practice.html')

def insert_data(request):
    insert_wine()
    insert_food()
    insert_review()
    return redirect('main')


