
from django.shortcuts import render
from . models import VisitInfo
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template

def index(request):
    return render(request, 'visit/index.html')

def check_in(request):
    return render(request, 'visit/checkin.html')

def check_out(request):
    return render(request, 'visit/checkout.html')

def check_in_submit(request):
    visitor_name = request.POST["visitor_name"]
    visitor_email = request.POST["visitor_email"]
    visitor_phone = request.POST["visitor_phone"]
    host_name = request.POST["host_name"]
    host_email = request.POST["host_email"]
    host_phone = request.POST["host_phone"]
    checkin_date_time = request.POST["checkin_date_time"]
    visit_info = VisitInfo(visitor_name=visitor_name, visitor_email=visitor_email,
                           visitor_phone=visitor_phone, host_name=host_name,
                           host_email=host_email, host_phone=host_phone,
                           checkin_date_time=checkin_date_time, checkout_date_time=checkin_date_time)
    visit_info.save()
    subject = 'You have a visitor'
    context = {
        'host_name': host_name,
        'visitor_name': visitor_name,
        'visitor_email': visitor_email,
        'visitor_phone': visitor_phone,
    }
    message = get_template('message.txt').render(context)
    send_mail(subject, message, 'test.ch.936@gmail.com', [host_email], fail_silently=False)
    return render(request, 'visit/index.html')

def check_out_submit(request):
    checkout_date_time = request.POST["checkout_date_time"]
    visitor_email = request.POST["visitor_email"]
    VisitInfo.objects.filter(visitor_email=visitor_email).update(checkout_date_time=checkout_date_time)
    visit_info1 = VisitInfo.objects.get(visitor_email=visitor_email)
    visitor_name = visit_info1.visitor_name
    visitor_phone = visit_info1.visitor_phone
    checkin_date_time = visit_info1.checkin_date_time
    checkout_date_time = visit_info1.checkout_date_time
    host_name = visit_info1.host_name
    host_email = visit_info1.host_email
    host_phone = visit_info1.host_phone

    subject = 'Visit summary'
    context = {
        'host_name': host_name,
        'visitor_name': visitor_name,
        'visitor_email': visitor_email,
        'visitor_phone': visitor_phone,
        'checkin_date_time' : checkin_date_time,
        'checkout_date_time' : checkout_date_time,
        'host_email' : host_email,
        'host_phone' : host_phone,
    }
    message = get_template('message1.txt').render(context)
    send_mail(subject, message, 'test.ch.936@gmail.com', [visitor_email], fail_silently=False)
    return render(request, 'visit/index.html')
