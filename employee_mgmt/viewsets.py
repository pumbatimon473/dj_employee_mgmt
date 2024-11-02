from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from employee_mgmt.filters import EmployeeFilter
from employee_mgmt.models import Employee
from employee_mgmt.pagination import SmallResultsSetPagination
from employee_mgmt.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    pagination_class = SmallResultsSetPagination

    def perform_destroy(self, instance: Employee):
        instance.is_deleted = True
        instance.save()
