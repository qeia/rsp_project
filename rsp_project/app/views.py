from django.shortcuts import render
from forms import EmployeeForm, StudentForm
from django.http import HttpResponse
from django.conf.urls import patterns
from django.contrib import admin
from django.core.mail import send_mail
import hashlib, datetime, random
from app.models import Employee, StudentRegister, Student

def startpage(request):
    return render(request, 'home_page.html')

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'finished.html')
        else:
            print form.errors
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def student_form(request, activation_key):
    ak=activation_key
    obj=StudentRegister.objects.filter(activation_key=ak)
    if len(obj) == 0:
        return render(request, "not_found.html")
    else:
        if request.method == 'POST':
            if obj[0].form_filled is True:
                return render(request,'already_filled.html')
            else:
                form = StudentForm(request.POST, request.FILES)
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.student_register = obj[0]

                    profile.save()
                    obj[0].student=profile
                    obj[0].save()
                    return render(request, 'finished.html')
                else:
                    print form.errors
        else:
            form = StudentForm()
        return render(request, 'student_form.html', {'form': form, 'name': StudentRegister.objects.filter(activation_key=ak)[0].employee.name_r})
def send_emails(request):
    for employee_iter in Employee.objects.all():
        email = employee_iter.email_id_r
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        activation_key_iter = hashlib.sha1(salt+email).hexdigest()
        key_expires_iter = datetime.datetime.today() + datetime.timedelta(2)
        new_profile = StudentRegister(employee=employee_iter, activation_key=activation_key_iter, key_expires=key_expires_iter)
        new_profile.save()
        email_subject = 'Account confirmation'
        email_body = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours" \
                     " siddharth1995.pythonanywhere/confirm/%s" % (new_profile.employee.name_r, activation_key_iter)
        send_mail(email_subject, email_body, 'ffifasiddharth@gmail.com', [email], fail_silently=False)
        print "sent email to %s" % new_profile.employee.name_r
        return HttpResponse("Sent")
import csv
def export(request):
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attatchment; filename="somefilename.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow(['Employee Name',
                     'Office Mobile Number',
                     'PL Number',
                     'Department',
                     'Designation',
                     'Email Id',
                     'Ward name',
                     'Ward Relation',
                     'Ward Sex',
                     'Ward Email',
                     'Ward Semester',
                     'Ward college name'])
    for obj in Employee.objects.all():
        studentregister = StudentRegister.objects.filter(employee=obj)
        student=Student.objects.filter(student_register=studentregister)
        writer.writerow([
            smart_str(obj.name),
            smart_str(obj.mobile_number_office),
            smart_str(obj.pi_number),
            smart_str(obj.department),
            smart_str(obj.designation),
            smart_str(obj.email_id),
            smart_str(obj.name_r),
            smart_str(obj.relation),
            smart_str(student[0].sex),
            smart_str(obj.email_id_r),
            smart_str(student[0].sem),
            smart_str(student[0].college_name)
        ])
    return response

def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('', (r'^csv/$', admin.site.admin_view(export)),
                           (r'^send_emails/$', admin.site.admin_view(send_emails)))
        return my_urls + urls
    return get_urls
admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls

