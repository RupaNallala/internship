from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    c_list=course.objects.all()
    return HttpResponse(c_list)
    