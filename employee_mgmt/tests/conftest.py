import pytest
from employee_mgmt.models import Employee
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture()
def user() -> User:
    return User.objects.create_user(username='sam', password='1234')

@pytest.fixture()
def employee() -> Employee:
    return Employee.objects.create(
        name='John Jhonson',
        email='john@jhonson.com',
        department='HR',
        role='MANAGER'
    )

@pytest.fixture()
def api_client() -> APIClient:
    """Fixture to provide an API client"""
    return APIClient()

@pytest.fixture()
def employee_small_payload() -> dict:
    """Fixture to provide an employee payload with only mandatory fields"""
    return {
        'name': 'Joe Dalton',
        'email': 'joe@dalton.com'
    }

@pytest.fixture()
def employee_large_payload() -> dict:
    """Fixture to provide an employee payload with all the optional fields"""
    return {
        'name': 'Joey Dalton',
        'email': 'joey@dalton.com'
    }
