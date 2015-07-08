from django.db import models
from django.contrib.auth.forms import User
import datetime

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=230, primary_key=True)
    pi_number = models.BigIntegerField()
    mobile_number_personal = models.BigIntegerField()
    mobile_number_office = models.BigIntegerField()
    mobile_number_residence = models.BigIntegerField()

    designation = models.CharField(max_length=40, )
    department = models.CharField(max_length=100,)
    name_r = models.CharField(max_length=30)

    email_id_r = models.EmailField(max_length=230)
    rel_choice = (
        ('s', 'Son'),
        ('d', 'Daughter'),
        ('or', 'Other')
    )
    relation = models.CharField(max_length=2, choices=rel_choice)


    def __str__(self):
        return self.email_id

class StudentRegister(models.Model):
    employee= models.ForeignKey(Employee, primary_key=True)

    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()
    form_filled = models.BooleanField(default=False)
    def __str__(self):
        return self.employee.email_id_r

class Student(models.Model):
    student_register = models.ForeignKey(StudentRegister, primary_key=True)
    college_name = models.CharField(max_length=250, default="nit")
    department_choice = models.CharField(max_length=100)
    duration_choice = (
        (15, 15),
        (30, 30),
        (45, 45),
        (60, 60)
    )
    duration = models.IntegerField(choices=duration_choice, default=15)

    picture = models.ImageField(upload_to='media', null=True)
    sex_choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    sem_choice = (
        (4, 4),
        (5, 5)
    )
    sem = models.IntegerField(choices=sem_choice, default = 4)
    sex = models.CharField(max_length=1, choices=sex_choice, default='M')
    branch = models.CharField(max_length=25)

    def __str__(self):
        return self.student_register.employee.email_id_r








