import django_filters
from employee_mgmt.models import Employee
from django.db.models.query import QuerySet

class EmployeeFilter(django_filters.FilterSet):
    # exclusive filter: allows excluding the mentioned department (or role) from the result
    department__not = django_filters.CharFilter(field_name='department', exclude=True)
    role__not = django_filters.CharFilter(field_name='role', exclude=True)
    # exclusive filter: allows excluding multiple departments (or roles) from the result
    department__not__in = django_filters.CharFilter(field_name='department', method='filter_department_not_in')
    role__not__in = django_filters.CharFilter(field_name='role', method='filter_role_not_in')

    @staticmethod
    def filter_department_not_in(queryset: QuerySet[Employee], _: str, value: str):
        return queryset.exclude(department__in=[val.upper().strip() for val in value.split(',')])

    @staticmethod
    def filter_role_not_in(queryset: QuerySet[Employee], _: str, value: str):
        return queryset.exclude(role__in=[val.upper().strip() for val in value.split(',')])

    class Meta:
        model = Employee
        fields = {
            'department': ['exact', 'in'],  # inclusive filter: department__in=['HR', 'ENGINEERING']
            'role': ['exact', 'in'],
        }