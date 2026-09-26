from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    p_list=Product.objects.all()
    return HttpResponse(p_list)