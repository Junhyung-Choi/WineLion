from django import forms
from django.db.models import fields
from django.db.models.base import Model

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

#views.py에서 RegisterForm을 불러와야 이제 유저 생성 form을 갖다 쓸 수 있다.
class RegisterForm(UserCreationForm):
    username = forms.CharField(label = '아이디', required=True)
    password1= forms.CharField(label = '비밀번호', required=True, widget = forms.PasswordInput)
    password2 = forms.CharField(label = '비밀번호 확인', required=True, widget = forms.PasswordInput)
    email = forms.EmailField(label = "이메일",required=False)
    birth = forms.DateField(label = "생년월일",required=True, widget = forms.DateInput)
    gender = forms.ChoiceField(label = "성별", choices=[("M","남성"),("F","여성")], required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2', 'email', 'birth', 'gender']


