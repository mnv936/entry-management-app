from django.db import models

# Create your models here.

class VisitInfo(models.Model):
    visitor_name = models.CharField(max_length=64)
    visitor_email = models.CharField(max_length=64)
    visitor_phone = models.IntegerField()
    host_name = models.CharField(max_length=64)
    host_email = models.CharField(max_length=64)
    host_phone = models.IntegerField()
    checkin_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkout_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
