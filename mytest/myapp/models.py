from django.db import models

# Create your models here.

class Departments(models.Model):
    dept_name = models.CharField(max_length=200)
    dept_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.dept_name


class Employees(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_id = models.IntegerField(primary_key=True)
    emp_dept = models.ForeignKey(Departments, on_delete=models.CASCADE)
    emp_surname = models.CharField(max_length=200)
    emp_email = models.EmailField(max_length=200)
    emp_photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.emp_name        