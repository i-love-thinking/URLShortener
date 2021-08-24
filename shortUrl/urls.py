"""shortUrl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app import views
from app.api import api
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from ninja import NinjaAPI



urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('', views.index),
    path('<str:shortenString>', views.redirect_to_page),
    path("api/", api.urls),
    path('not_found/',views.not_found),
    # path('admin/', admin.site.urls),
]
