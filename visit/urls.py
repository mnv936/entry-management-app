from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("check_in", views.check_in, name='check_in'),
    path("check_out", views.check_out, name='check_out'),
    path("check_in_submit", views.check_in_submit, name='check_in_submit'),
    path("check_out_submit", views.check_out_submit, name='check_out_submit'),
]
