from rest_framework import serializers
from employee_mgmt.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        instance_dict = super().to_representation(instance)
        instance_dict['date_joined'] = instance_dict.get('created_at')
        return instance_dict
