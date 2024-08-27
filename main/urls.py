from django.urls import re_path
from . import views


urlpatterns=[
    re_path(r'^api/students/$', views.students_list),
    re_path(r'^api/students/([0-9])$', views.students_detail),
   
]