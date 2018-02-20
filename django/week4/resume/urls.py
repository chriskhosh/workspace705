from django.conf.urls import include, url
from django.contrib import admin
from resume import views

app_name="resume"

urlpatterns = [
    url(r'^$', views.home, name="home"),
]
