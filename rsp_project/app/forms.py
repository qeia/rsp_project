from django import forms
from models import Employee
from models import Student

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label="  Enter your name",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_id = forms.EmailField(max_length=230, label="  Enter your email id",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    pi_number = forms.IntegerField(label="Enter your PI number",
                                   widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mobile_number_personal = forms.IntegerField(label ="Enter your personal mobile number",
                                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mobile_number_office = forms.IntegerField(label ="Enter your office mobile number",
                                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mobile_number_residence = forms.IntegerField(label ="Enter your residence number",
                                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(max_length=50, label="Enter your designation",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField(max_length=100, label="Enter your department",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    name_r = forms.CharField(max_length=30, label="Enter your ward's name",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_id_r = forms.EmailField(max_length=230, label="Enter your ward's Email Id",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        exclude = ()

class StudentForm(forms.ModelForm):
    college_name = forms.CharField(max_length=250, label="Enter your college name",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    department_choice = forms.IntegerField(max_value=10, label="Enter the department choice",
                                           widget=forms.NumberInput(attrs={'class': 'form-control'}))
    duration = forms.CharField(max_length=250, label="Enter the duration",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(max_length=250, label="Enter your gender",
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    branch = forms.CharField(max_length=250, label="Enter your branch",
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    picture = forms.FileField()

    class Meta:
        model = Student
        exclude = ()

