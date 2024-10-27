from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import TemplateResponseMixin, ContextMixin
from django.views import View
from users.models import UserData
from django.contrib.auth.models import User

import requests
import json


class HomePage(TemplateView):
    template_name = "app/home-page.html"


class FindRestaurantView(LoginRequiredMixin, TemplateView):
    template_name = "app/find-restaurant.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not UserData.objects.filter(user=self.request.user).exists():
            data = UserData(user=self.request.user)
            data.save()
        else:
            data = UserData.objects.filter(user=self.request.user)

        context["user_data"] = data
        print(data.calendar)

        return context


class UserTasks(TemplateResponseMixin, ContextMixin, View):
    template_name = "app/show-tasks.html"

    def get(self, request):
        context = self.get_context_data()

        if "calendar_url" in request.GET:
            data = json.loads(requests.get(f"http://ranged-model:8125/events/get?calendar_url={request.GET['calendar_url']}").text)
            context["events"] = data

        return super().render_to_response(context)
