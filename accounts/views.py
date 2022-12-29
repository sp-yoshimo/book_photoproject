from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    #サインアップのビュー

    form_class=CustomUserCreationForm

    template_name="signup.html"
    success_url=reverse_lazy("accounts:signup_success")

    def form_invalid(self, form):

        user=form.save()
        self.object=user

        return super().form_invalid(form)


class SignUpSuccessView(TemplateView):
    #サインアップ成功ビュー
    template_name="signup_success.html"