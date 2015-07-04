from django import forms
from models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from models import Student
class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label="  Enter your first name")
    last_name = forms.CharField(max_length=30, label="  Enter your last name")
    email_id = forms.EmailField(max_length=230, label="  Enter your email id")
    mobile_number = forms.IntegerField(label ="Enter your mobile number")
    first_name_r = forms.CharField(max_length=30, label = "Enter your relative's first name")
    last_name_r = forms.CharField(max_length=30, label = "Enter your relative's last name")
    email_id_r = forms.EmailField(max_length=230, label = "Enter your relative's Email Id")

    class Meta:
        model = Employee
        exclude = ()

class StudentForm(forms.ModelForm):
    college_name = forms.CharField(max_length = 250, label="Enter your college name", widget=forms.TextInput(attrs={'class':'form-control'}))
    department_choice = forms.IntegerField(max_value=10, label="Enter the department choice", widget=forms.NumberInput(attrs={'class':'form-control'}))
    picture = forms.FileField()
    class Meta:
        model = Student
        fields = ('college_name','department_choice','picture', )


    '''def save(self, studentregister):
        data = self.cleaned_data
        student=Student(student_register = studentregister, college_name = data['college_name'], department_choice = data['department_choice'])
        student.student_register.form_filled=True
        student.student_register.save()
        student.save()'''

