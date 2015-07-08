import os


from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'rsp_project.settings'
application = get_wsgi_application()
from django.core.mail import send_mail
import hashlib, datetime, random

from app.models import Employee, StudentRegister, Student


for employee_iter in Employee.objects.all():

    email = employee_iter.email_id_r
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    activation_key_iter = hashlib.sha1(salt+email).hexdigest()
    key_expires_iter = datetime.datetime.today() + datetime.timedelta(2)
    new_profile = StudentRegister(employee=employee_iter, activation_key=activation_key_iter, key_expires=key_expires_iter)
    new_profile.save()

    email_subject = 'Account confirmation'
    email_body = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours siddharth1995.pythonanywhere/confirm/%s" % (new_profile.employee.first_name_r, activation_key_iter)

    send_mail(email_subject,email_body,[email],fail_silently=False)
    print "sent emmail to %s" %new_profile.employee.first_name_r