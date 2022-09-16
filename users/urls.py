from django.urls import path

from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('register/', RegisterUserView.as_view(), name='register_user')
]
