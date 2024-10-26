from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
