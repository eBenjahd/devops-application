from django.urls import path
from consultor.views import (
    RegisterView,
    LoginView,
    CookieTokenRefreshView,
    UserMeView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", CookieTokenRefreshView.as_view(), name="refresh"),
    path("me/", UserMeView.as_view(), name="me"),
]