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

    def post(self, request, *args, **kwargs):
        data = UserData.objects.filter(user=request.user)[0]
        data.calendar = request.POST["calendar_url"]
        data.save()

        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not UserData.objects.filter(user=self.request.user).exists():
            data = UserData(user=self.request.user)
            data.save()
        else:
            data = UserData.objects.get(user=self.request.user)

        context["user_data"] = data

        if data.calendar:
            events = json.loads(
                requests.post("http://ranged-model:8125/events/get", json={"calendar_url": data.calendar}).text
            )
            context["events"] = events["events"]

            locations = json.loads(
                requests.post("http://ranged-model:8125/locations/get", json={"location": "2-я Бауманская, 5с1"}).text
            )

            x = list()

            for _, value in locations.items():
                x.append(value)

            ranking = json.loads(
                requests.post("http://ranged-model:8125/model/ranking", json={
                    "x": x,
                    "weights": [2.16865241, 0.19021977, 0.51186798, 0.76699442, 1.16699469]
                }).text
            )["ranked"]

            restik = list()
            for rank in ranking:
                restik.append(list(locations.keys())[rank])

            context["restiks"] = restik

        return context


class UserTasks(TemplateResponseMixin, ContextMixin, View):
    template_name = "app/show-tasks.html"

    def get(self, request):
        context = self.get_context_data()

        if "calendar_url" in request.GET:
            data = json.loads(requests.get(f"http://ranged-model:8125/events/get?calendar_url={request.GET['calendar_url']}").text)
            context["events"] = data

        return super().render_to_response(context)
