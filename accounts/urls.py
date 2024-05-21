from django.urls import path
from .views import *
from website.views import login

urlpatterns = [
    path('login/',login.as_view(),name="login"),
]


