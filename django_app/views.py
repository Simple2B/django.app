from django.shortcuts import redirect
from urllib import request


def home_page(request):
    return redirect('posts_list')
