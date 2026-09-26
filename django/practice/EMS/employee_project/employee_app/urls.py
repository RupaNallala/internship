from django.urls import path
from employee_app import views
urlpatterns = [
    path('',views.index,name='index'),
]