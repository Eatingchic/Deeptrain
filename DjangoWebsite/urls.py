"""DjangoWebsite URL Configuration

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
from django.conf.urls import url
from django.views import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
import views
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("favicon.ico", RedirectView.as_view(url="/static/images/favicon.ico")),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
    path("admin/", admin.site.urls, name="admin"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("change/", views.change, name="change"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("im/", include(("im.urls", "im")), name="im"),
    path("applications/", include(("applications.urls", "applications")), name="applications"),
    path("files/", include(("files.urls", "files")), name="files"),
    path("geoip/", include(("geoip.urls", "geoip")), name="geoip"),
    path("monitor/", include(("monitor.urls", "monitor")), name="monitor"),
]
