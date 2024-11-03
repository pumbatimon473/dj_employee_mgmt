import pytest
import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

def random_str(n: int, lb: int=97, ub: int=122) -> str:
    """
    Returns a random str of the specified len
    @:param lb: lower bound of the ASCII char range
    @:param ub: upper bound of the ASCII char range
    """
    import random
    return ''.join([chr(random.randrange(lb, ub+1)) for _ in range(n)])

@pytest.mark.django_db
def test_employee_name_char_limit(employee):
    employee.name = random_str(65)  # exceeds the max char len 64
    with pytest.raises(ValidationError) as e:
        employee.full_clean()
    logger.info(f'e.value: {e.value}')
    assert 'Ensure this value has at most 64 characters' in str(e.value)

@pytest.mark.django_db
def test_employee_name_should_not_accept_only_spaces(employee):
    employee.name = '   '  # only whitespaces
    with pytest.raises(ValidationError) as e:
        employee.full_clean()
    logger.info(f'e.value: {e.value}')
    assert 'Only english alphabets are allowed with names separated by spaces' in str(e.value)

@pytest.mark.django_db
def test_employee_email_validation(employee):
    employee.email = 'one@two@invalid.com'  # more than one @ in the email
    with pytest.raises(ValidationError) as e:
        employee.full_clean()
    logger.info(f'e.value: {e.value}')
    assert 'Enter a valid email address' in str(e.value)
