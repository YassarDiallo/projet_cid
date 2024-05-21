from django.contrib import admin
from django.urls import path,include
from django.conf  import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('',login.as_view(),name="login"),
    path('logout/',Logout.as_view(),name="logout"),
    path('home/', login_required(home),name="home"),
    path('admin/', admin.site.urls),
    path('documents/',include('documents.urls')),
    path('accounts/',include('accounts.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


