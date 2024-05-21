from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth  import views
from .models import CustomUser
from .forms import UserForm


class register(CreateView):
    model=CustomUser
    form_class=UserForm
    template_name="registrations/register.html"
    success_url=reverse_lazy('login')


