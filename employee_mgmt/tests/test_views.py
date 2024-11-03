import pytest
import logging
from rest_framework import status
from employee_mgmt.models import Department, Role

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_employee_with_only_required_fields(api_client, employee_small_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee: send a post request with the authenticated user
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    logger.info(f'{response_create.data}')
    assert response_create.status_code == status.HTTP_201_CREATED
    assert response_create.data['name'] == employee_small_payload['name']
    # read the newly created employee
    response_read = api_client.get('/api/employees/')
    assert response_read.data['count'] == 1
    assert response_read.data['results'][0]['email'] == employee_small_payload['email']

@pytest.mark.django_db
def test_update_employee_email_unique(api_client, employee_small_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    employee_id = response_create.data['id']
    logger.info(f'Created a new employee with id {employee_id}')
    assert response_create.status_code == status.HTTP_201_CREATED
    assert response_create.data['email'] == employee_small_payload['email']
    # update the email id: send the put request with the authenticated user
    old_email = employee_small_payload['email']
    employee_small_payload['email'] = 'william@dalton.com'
    response_update = api_client.put(f'/api/employees/{employee_id}/', data=employee_small_payload)
    new_email = response_update.data['email']
    logger.info(f'Updated the employee with id {employee_id}')
    logger.info(f'New email id is "{new_email}"; was "{old_email}"')
    assert response_update.status_code == status.HTTP_200_OK
    assert response_update.data['email'] == employee_small_payload['email']

@pytest.mark.django_db
def test_partial_update_employee_assign_department_and_role(api_client, employee_small_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    employee_id = response_create.data['id']
    logger.info(f'Created a new employee with id {employee_id}')
    assert response_create.status_code == status.HTTP_201_CREATED
    assert response_create.data['email'] == employee_small_payload['email']
    # partial update: send patch request
    update_payload = {
        'department': Department.SALES,
        'role': Role.ANALYST
    }
    response_partial_update = api_client.patch(f'/api/employees/{employee_id}/', data=update_payload)
    logger.info(f'Assigned department and role to the employee with id {employee_id}')
    assert response_partial_update.status_code == status.HTTP_200_OK
    assert response_partial_update.data['department'] == Department.SALES
    assert response_partial_update.data['role'] == Role.ANALYST

@pytest.mark.django_db
def test_delete_employee(api_client, employee_small_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    employee_id = response_create.data['id']
    logger.info(f'Created a new employee with id {employee_id}')
    assert response_create.status_code == status.HTTP_201_CREATED
    assert response_create.data['email'] == employee_small_payload['email']
    # delete the employee: send a delete request
    response_delete = api_client.delete(f'/api/employees/{employee_id}/')
    logger.info(f'Deleted employee with id {employee_id}')
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT
    # deleted employee not found
    response_retrieve = api_client.get(f'/api/employees/{employee_id}/')
    assert response_retrieve.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_create_employee_with_duplicate_email_not_allowed(api_client, employee_small_payload, employee_large_payload,
                                                          user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    logger.info(f'Created a new employee with email "{response_create.data['email']}"')
    assert response_create.status_code == status.HTTP_201_CREATED
    # create another employee with the same email id
    logger.info(f'Creating another employee with the same email id ...')
    employee_large_payload['email'] = employee_small_payload['email']
    response_create_2 = api_client.post('/api/employees/', data=employee_large_payload)
    assert response_create_2.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_employee_with_name_containing_only_spaces_not_allowed(api_client, employee_small_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee
    employee_small_payload['name'] = '   '  # name containing spaces only
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    logger.info(f'{response_create.data}')
    assert response_create.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_partial_update_employee_with_name_containing_digits_not_allowed(api_client, employee_small_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    # create a new employee
    response_create = api_client.post('/api/employees/', data=employee_small_payload)
    logger.info(f'{response_create.data}')
    assert response_create.status_code == status.HTTP_201_CREATED
    assert response_create.data['name'] == employee_small_payload['name']
    # update the employee's name with name containing digits
    employee_id = response_create.data['id']
    update_payload = {'name': 'Joe Since 1968'}  # name containing digits
    logger.info(f"Updating the employee's name with '{update_payload['name']}'")
    response_partial_update = api_client.patch(f'/api/employees/{employee_id}/', data=update_payload)
    logger.info(f'{response_partial_update.data}')
    assert response_partial_update.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_accessing_employees_endpoint_requires_authentication(api_client):
    response_list = api_client.get('/api/employees/')
    logger.info(f'{response_list.data}')
    assert response_list.status_code == status.HTTP_401_UNAUTHORIZED
