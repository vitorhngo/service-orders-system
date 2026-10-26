from django.db import transaction
from .models import User, EmployeeProfile
from ..companies.models import Company


@transaction.atomic
def create_company_with_admin(company_data, user_data):
    company = Company.objects.create(
        name=company_data["name"], email=company_data["email"]
    )

    user = User.objects.create_user(
        username=str(company.pk) + "-" + user_data["full_name"],
        full_name=user_data["full_name"],
        password=user_data["password1"],
    )

    employee_profile = EmployeeProfile.objects.create(user=user, company=company)

    return company, user, employee_profile
