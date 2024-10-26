from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.SignUp.as_view(), name="login"),
]
