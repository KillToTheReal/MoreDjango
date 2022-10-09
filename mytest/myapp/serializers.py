from rest_framework import serializers
from myapp.models import Departments,Employees

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('dept_id','dept_name')
        
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('emp_id','emp_name','emp_surname','emp_email','emp_photo','emp_dept')