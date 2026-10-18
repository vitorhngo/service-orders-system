from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.accounts, name="accounts"),
    path("profile", views.profile, name="profile"),
    path(
        "sign-in",
        auth_views.LoginView.as_view(template_name="accounts/sign_in.html"),
        name="sign-in",
    ),
    path("sign-out", views.sign_out, name="sign-out"),
    path("sign-up", views.sign_up, name="sign-up"),
]
