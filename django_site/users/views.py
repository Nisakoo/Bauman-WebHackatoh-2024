from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .forms import RegistrationForm


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("main:find")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return HttpResponseRedirect(self.success_url)
