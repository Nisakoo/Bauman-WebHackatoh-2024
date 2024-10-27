from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    calendar = models.CharField(max_length=1024, default="", blank=False)
