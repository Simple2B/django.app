from urllib import request
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q

from .forms import UserCreateForm, LoginUserForm
from .models import CustomUser
from .logger import logger


class RegisterUserView(CreateView):
    form_class = UserCreateForm
    template_name = "users/register_user.html"
    success_url = reverse_lazy("register_user")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("posts_list")


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "users/login_page.html"

    def get_success_url(self) -> str:
        return reverse_lazy("posts_list")


def logout_user(request):
    logout(request)
    return redirect("login_user")


class UserListView(ListView):
    model = CustomUser
    template_name = "users/profiles.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return CustomUser.objects.filter(
            ~Q(pk=self.request.user.pk), is_superuser=False
        )
