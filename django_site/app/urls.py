from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("find", views.FindRestaurantView.as_view(), name="find"),
    path("tasks", views.UserTasks.as_view(), name="tasks")
]
