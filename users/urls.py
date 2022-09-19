from django.urls import path

from .views import *


urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout')
]
