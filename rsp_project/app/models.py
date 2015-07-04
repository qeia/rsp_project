from django.db import models
from django.contrib.auth.forms import User
import datetime

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=230, primary_key=True)
    mobile_number = models.BigIntegerField()
    first_name_r = models.CharField(max_length=30)
    last_name_r = models.CharField(max_length=30)
    email_id_r = models.EmailField(max_length=230)
    def __str__(self):
        return self.email_id

class StudentRegister(models.Model):
    employee= models.ForeignKey(Employee, primary_key=True)

    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()
    form_filled = models.BooleanField(default =False)
    def __str__(self):
        return self.employee.email_id_r

class Student(models.Model):
    student_register = models.ForeignKey(StudentRegister, primary_key=True)
    college_name = models.CharField(max_length = 250, default="nit")
    department_choice = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.student_register.employee.email_id_r








