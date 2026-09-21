from django.urls import path

from consultor.views import AskView, DoubtView

urlpatterns = [
    path("ask/", AskView.as_view(), name="ask"),
    path("doubt/", DoubtView.as_view(), name="doubt"),
]