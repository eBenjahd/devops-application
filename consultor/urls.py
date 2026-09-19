from django.urls import path
from consultor.views import AskView


urlpatterns = [
    path("ask/", AskView.as_view(), name="ask"),
]