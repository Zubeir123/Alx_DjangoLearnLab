from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, register, profile, home
)

urlpatterns = [
    path('', home, name='home'),

    # Auth
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    # path('pos/', pos_page, name='pos'),
]


