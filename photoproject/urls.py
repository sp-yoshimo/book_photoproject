from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #photo.urlsへのURLパターン
    path("",include("photo.urls")),

    #accounts.urlへのURLパターン
    path("",include("accounts.urls")),

    #パスワードリセットのためのURLパターン
    #PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載

    #パスワードリセット申し込みページ
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="password_reset"),

    #メール送信完了ページ
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),

    #パスワードリセットページ
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),

    #パスワードリセット完了ページ
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete")
]


#urlpatternsにmediaフォルダーのURLパターンを追加
urlpatterns+=static(
    #MEDIA_URL="media/"
    settings.MEDIA_URL,
    #MEDIA_URLにリダイレクト
    document_root=settings.MEDIA_ROOT
)