
from django.http import HttpResponseRedirect
from django.contrib.auth  import views
from django.shortcuts import render
from django.urls import reverse_lazy


def home(request):
    return render(request,'home.html')


class login(views.LoginView):
    template_name="registrations/login.html"
    

class Logout(views.LogoutView):
    template_name="registrations/logout.html"
    success_url=reverse_lazy('login')