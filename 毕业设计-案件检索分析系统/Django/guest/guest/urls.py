"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from sign import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/', views.index),
    url(r'^accounts/login/$', views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^menu/$', views.menu),
    url(r'^Insert/$', views.Insert),
    url(r'^select_delate_fix/$', views.Select_delate_fix),
    url(r'^pie/$', views.Pie),
    url(r'^line/$', views.Line),
    url(r'^histogram/$', views.Histogram),
    url(r'^china/$', views.China),
    url(r'^cover/$', views.Cover),
    url(r'^insert_max_data/$', views.Insert_max_data),
    url(r'^details/$', views.Details),
    url(r'^fix/$', views.Fix),
    url(r'^delate/$', views.Delate),
]
