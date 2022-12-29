from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost

# Create your views here.

class IndexView(ListView):
    template_name="index.html"

    #投稿日時の降順で並び変える
    queryset=PhotoPost.objects.order_by("-posted_at")

    #1ページに表示するレコードの件数
    paginate_by=9

#デコレーターにより、ログイン中にのみこのビューを実行できる
@method_decorator(login_required,name="dispatch")
class CreatePhotoView(CreateView):
    #写真投稿ページのビュー
    
    #PhotoPostで定義されているモデルとフィールドを連携して投稿データをデータベースに登録する

    #forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class=PhotoPostForm
    #レンダリングするテンプレート
    template_name="post_photo.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url=reverse_lazy("photo:post_done")

    def form_valid(self, form):
        #フォームが送信された際に呼び出される関数

        #POSTデータを取得
        postdata=form.save(commit=False)
        #投稿データのidを取得してモデルのuserフィールドに格納
        postdata.user=self.request.user
        #投稿データをデータベースに登録
        postdata.save()

        return super().form_valid(form)


class PhotoSuccessView(TemplateView):
    #投稿完了ページのビュー

    #レンダリングするファイル
    template_name="post_success.html"


class CategoryView(ListView):
    #カテゴリページのビュー

    #index.htmlをレンダリングする
    template_name="index.html"
    #1ページに表示するレコードの件数
    paginate_by=9

    def get_queryset(self):
        #クエリを実行する

        #self.kwargsの取得が必要なためクラス変数querysetではなく、get_queryset()のオーバーライドにてクエリを実行する
        
        #カテゴリのidを取得する
        category_id=self.kwargs["category"]
        #filter(フィールド名=id)絞り込む
        categories=PhotoPost.objects.filter(category=category_id).order_by("-posted_at")
        
        #クエリによって取得されたレコードを返す
        return categories


class UserView(ListView):
    #ユーザーの投稿一覧ページのビュー

    #index.htmlをレンダリングする
    template_name="index.html"
    #１ページに表示するレコードの件数
    paginate_by=9

    def get_queryset(self):
        #クエリを実行する

        #userキーの値を取得
        user_id=self.kwargs["user"]
        #fillterで絞り込む
        user_list=PhotoPost.objects.filter(user=user_id).order_by("-posted_at")

        #レコードを返す
        return user_list

class DetailView(DetailView):
    #詳細ページのビュー

    #投稿記事の詳細を表示するのでDetailViewを継承する

    #detail.htmlをレンダリングする
    template_name="detail.html"
    #クラス変数modelにモデルPhotoPostを定義
    model=PhotoPost


class MypageView(ListView):
    #マイページのビュー

    #mypage.htmlをレンダリングする
    template_name="mypage.html"
    #1ページに表示するレコードの件数
    paginate_by=9

    def get_queryset(self):
        #クエリの実行

        #現在ログインしているユーザー名はHttpResoponce.userに格納されている
        queryset=PhotoPost.objects.filter(user=self.request.user).order_by("-posted_at")

        return queryset


class PhotoDeleteView(DeleteView):
    #レコードの削除を行うビュー

    #操作の対象はPhotoPostモデル
    model=PhotoPost
    #photo_delete.htmlをレンダリング
    template_name="photo_delete.html"
    #処理完了後のマイページにリダイレクト
    success_url=reverse_lazy("photo:mypage")

    def delete(self,request,*args,**kwargs):
        #レコードの削除を行う

        #スーパークラスのdelete()を実行
        return super().delete(request,*args,**kwargs)