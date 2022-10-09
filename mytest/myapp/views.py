from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from myapp.models import Departments,Employees
from myapp.serializers import DepartmentsSerializer,EmployeesSerializer
from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentsSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)

    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        department=JSONParser().parse(request)
        department=Departments.objects.get(dept_id=department['dept_id'])
        departments_serializer=DepartmentsSerializer(department,data=department)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(dept_id=id)
        department.delete()
        return JsonResponse("Deleted Successfully!",safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)

    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        employee=JSONParser().parse(request)
        employee=Employees.objects.get(emp_id=employee['emp_id'])
        employees_serializer=EmployeesSerializer(employee,data=employee)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(emp_id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!",safe=False)    

@csrf_exempt
def saveImage(request): 
    if request.method == 'POST': 
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)  
        return JsonResponse(file_name,safe=False)
    else:
        return JsonResponse("Failed to Upload.",safe=False)