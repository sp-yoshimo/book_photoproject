from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    #ModelFormのサブクラス

    class Meta:
        #ModelFormのインナークラス
        model=PhotoPost #モデルのクラス
        fields=["category","title","comment","image1","image2"] #フォームで使用するモデルのフィールド