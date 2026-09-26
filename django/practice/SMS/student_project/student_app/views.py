from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def index(request):
    s_list=student.objects.all()
    return HttpResponse(s_list)