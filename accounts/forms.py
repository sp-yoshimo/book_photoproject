from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    #UserCreationFormのサブクラス

    class Meta:
        #連携するUserモデルを設定
        model=CustomUser
        #フォームで使用するフィールドを設定
        fields=("username","email","password1","password2")