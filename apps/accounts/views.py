from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from ..companies.forms import CompanyCreationForm
from .transactions import create_company_with_admin


@login_required
def accounts(request):
    """Accounts page"""
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
    return redirect("sign-in")


def register_company(request):
    """Get basic information to register a company."""
    if request.method != "POST":
        session_data = request.session.get("company_data", None)
        form = CompanyCreationForm(initial=session_data)
    else:
        form = CompanyCreationForm(request.POST)

        if form.is_valid():
            request.session["company_data"] = form.cleaned_data
            return redirect("register-user")

    return render(request, "accounts/register_company.html", {"form": form})


def register_user(request):
    """Get basic information to register the company's first administrator."""
    company_data = request.session.get("company_data")

    if not company_data:
        return redirect("register-company")

    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            request.session["user_data"] = form.cleaned_data
            return redirect("sign-up")

    return render(request, "accounts/register_user.html", {"form": form})


def sign_up(request):
    """Ensures the complete creation of the company and administrator user."""

    company_data = request.session.get("company_data")
    user_data = request.session.get("user_data")
    if not company_data:
        return redirect("register-company")
    if not user_data:
        return redirect("register-user")

    _, user, _ = create_company_with_admin(company_data, user_data)
    authenticated_user = authenticate(
        username=user.username, password=user_data["password1"]
    )
    if authenticated_user:
        auth_login(request, authenticated_user)

        if request.session["company_data"]:
            del request.session["company_data"]
        if request.session["user_data"]:
            del request.session["user_data"]

        return redirect("profile")
