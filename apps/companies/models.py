from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=320, unique=True)
    cnpj = models.CharField(
        max_length=14, null=True
    )  # It can be null for debugging purposes. XXX: Change in production.

    def __str__(self) -> str:
        return self.name
