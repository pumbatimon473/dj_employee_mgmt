from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from employee_mgmt.models import Employee
from employee_mgmt.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance: Employee):
        instance.is_deleted = True
        instance.save()
