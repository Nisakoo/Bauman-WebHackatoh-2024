from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import TemplateResponseMixin, ContextMixin
from django.views import View

import requests
import json


class HomePage(TemplateView):
    template_name = "app/home.html"


class UserTasks(TemplateResponseMixin, ContextMixin, View):
    template_name = "app/show_tasks.html"

    def get(self, request):
        context = self.get_context_data()

        if "calendar_url" in request.GET:
            data = json.loads(requests.get(f"http://ranged-model:8125/events/get?calendar_url={request.GET['calendar_url']}").text)
            context["events"] = data

        return super().render_to_response(context)
