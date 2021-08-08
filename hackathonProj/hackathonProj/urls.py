"""hackathonProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hackathonApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main,name='main'),
    path('wine_info/<int:id>/',wine_info, name = "wine_info"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('base/', base, name = "base"),
    path('signup/', signup, name = "signup"),
    path('mypage/', mypage, name = "mypage")
    #   path('datas/',insert_data,name= 'insert_data')   # //DB 입력이 끝나서 주석처리해둠. db.sqlite3 파일을 지우지 않는한 활성화 시키지 말 것
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)