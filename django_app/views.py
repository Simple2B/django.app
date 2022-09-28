from django.shortcuts import redirect
from urllib import request
from .worker import webhook_request


def home_page(request):
    return redirect("posts_list")


def worker(request):
    if request.method == "GET":
        webhook_request()
    return redirect("register_user")
