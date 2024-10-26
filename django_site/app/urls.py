from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("tasks", views.UserTasks.as_view(), name="tasks")
]
