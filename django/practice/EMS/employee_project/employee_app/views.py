from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def index(request):
    e_list=Employee.objects.all()
    return HttpResponse(e_list)