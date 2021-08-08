from django import forms
from django.db.models import fields
from django.db.models.base import Model

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

#views.py에서 RegisterForm을 불러와야 이제 유저 생성 form을 갖다 쓸 수 있다.
class RegisterForm(UserCreationForm):
    birth = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=[("M","남성"),("F","여성")], required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2', 'birth', 'gender']


