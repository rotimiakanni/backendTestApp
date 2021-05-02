from .models import Employees
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = '__all__'

    def create(self, validated_data):
        employee = Employees(
            employee_id = validated_data['employee_id'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            age = validated_data['age'],
            join_date = validated_data['join_date']
        )
        employee.save()