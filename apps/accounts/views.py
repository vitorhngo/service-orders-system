from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def accounts(request):
    """accounts page"""
    # TODO: Add auth for company-admins
    # TODO: Redirect non-company-admins to their profile
    return render(request, "accounts/accounts.html")


@login_required
def profile(request):
    """User profile"""
    # TODO: Add profile_id to display especific user profile
    return render(request, "accounts/profile.html")


def sign_out(request):
    """Logs out the user."""
    auth_logout(request)
    return HttpResponseRedirect(reverse("sign-in"))


def sign_up(request):
    """Register a new user in the system."""
    if request.method != "POST":
        # Ensures that an authenticated user cannot access the registration page.
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("profile"))
        # No data submitted; displays a blank registration form.
        form = UserCreationForm()
    else:
        # POST data submitted; processes the registration form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Logs the user in and redirects them to the profile page.
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST["password1"]
            )
            auth_login(request, authenticated_user)
            return HttpResponseRedirect(reverse("profile"))

    context = {"form": form}

    return render(request, "accounts/sign_up.html", context)
