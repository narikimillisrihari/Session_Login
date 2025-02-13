from django.urls import path
from app1.views import LoginUser,LogoutUser,Registerserailizer,RegisterUser


urlpatterns = [
    path('login/',LoginUser.as_view(),name="register"),
    path('register/',RegisterUser.as_view(),name="login")
]