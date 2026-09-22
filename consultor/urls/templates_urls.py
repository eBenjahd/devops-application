from django.urls import path

from consultor.views.templates import home

urlpatterns = [
    path("", home, name="home"),
]