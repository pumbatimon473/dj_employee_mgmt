from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(models.TextChoices):
    HR = "HR", _("HR")
    ENGINEERING = "ENGINEERING", _("Engineering")
    SALES = "SALES", _("Sales")


class Role(models.TextChoices):
    MANAGER = "MANAGER", _("Manager")
    DEVELOPER = "DEVELOPER", _("Developer")
    ANALYST = "ANALYST", _("Analyst")


class Employee(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128, unique=True)
    department = models.CharField(max_length=32, choices=Department, blank=True)
    role = models.CharField(max_length=32, choices=Role, blank=True)
