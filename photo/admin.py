from django.contrib import admin
from .models import Category,PhotoPost

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    #管理ページに表示するカラムを設定するクラス

    list_display=("id","title")
    list_display_links=("id","title")


class PhotoPostAdmin(admin.ModelAdmin):
    #管理ページに表示するカラムを設定するクラス

    list_display=("id","title")
    list_display_links=("id","title")

#Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category,CategoryAdmin)

#Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(PhotoPost,PhotoPostAdmin)