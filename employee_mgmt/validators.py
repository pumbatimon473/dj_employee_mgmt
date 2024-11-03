from django.core.validators import RegexValidator

# Matches the below patterns for names:
# - first_name
# - first_name last_name
# - first_name middle_name last_name
name_validator = RegexValidator(r'^[a-zA-Z]+(\s[a-zA-Z]+){0,2}$',
                                'Only english alphabets are allowed with names separated by spaces')