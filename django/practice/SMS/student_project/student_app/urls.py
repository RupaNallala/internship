from django.urls import path
from student_app import views
ulrpatterns=[
    path('',view.index,name=index)
]