from django.shortcuts import render
from forms import EmployeeForm, StudentForm
from models import Student, StudentRegister
from django.http import HttpResponse

from app.models import Employee, StudentRegister, Student

def startpage(request):
    return render(request, 'home_page.html')

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print "afkjf"

        if form.is_valid():
            print "afojfo"
            form.save(commit = True)
            return HttpResponse("done")

        else:
            print form.errors
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})

def student_form(request, activation_key):
    ak=activation_key
    obj=StudentRegister.objects.filter(activation_key=ak)
    if len(obj)==0:
        return render(request,"not_found.html")
    else:
        if request.method == 'POST':
            if obj[0].form_filled==True:
                return render(request,'already_filled.html')
            else:
                form = StudentForm(request.POST, request.FILES)
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.student_register=obj[0]
                    profile.save()
                    return render(request, 'finished.html')
                else:
                    print form.errors

        else:
            form = StudentForm()
        return render(request, 'student_form.html', {'form': form, 'name': StudentRegister.objects.filter(activation_key=ak)[0].employee.first_name_r})







