from django.urls import path
from . import views

app_name="photo"

urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),

    #写真投稿ページ
    path("post/",views.CreatePhotoView.as_view(),name="post"),

    #投稿完了ページ
    path("post-done/",views.PhotoSuccessView.as_view(),name="post_done"),

    #カテゴリ一覧ページ
    path("photos/<int:category>",views.CategoryView.as_view(),name="photos_cat"),

    #ユーザーの投稿一覧ページ
    path("user-list/<int:user>",views.UserView.as_view(),name="user_list"),

    #詳細ページ
    #<int:pk>は辞書{pk:id値}としてDetailViewに渡される
    path("photo-detail/<int:pk>",views.DetailView.as_view(),name="photo_detail"),

    #マイページ
    path("mypage/",views.MypageView.as_view(),name="mypage"),

    #投稿写真の削除
    path("photo/<int:pk>/delete/",views.PhotoDeleteView.as_view(),name="photo_delete")
]
