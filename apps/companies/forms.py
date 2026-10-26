from django import forms
from .models import Company


class CompanyCreationForm(forms.ModelForm):
    """A form for creating new companies"""

    class Meta:
        model = Company
        fields = ["name", "email"]
        labels = {"name": "Nome da empresa", "email": "E-mail corporativo"}
