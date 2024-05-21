from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create/',login_required(create.as_view()),name="documents_create"),
    path('',index.as_view(),name="documents_index"),
    path('edit/<int:pk>/',edit.as_view(),name="documents_edit"),
    path('delete/<int:pk>/',delete.as_view(),name="documents_delete"),
]
