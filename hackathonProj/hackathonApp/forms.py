from django import forms
from django.db.models import fields
from django.db.models.base import Model

from django.contrib.auth.forms import UserCreationForm

from .models import Blog, CustomUser

#views.py에서 RegisterForm을 불러와야 이제 유저 생성 form을 갖다 쓸 수 있다.
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password','password2','grade']