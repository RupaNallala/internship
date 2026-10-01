from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    c_list=Course.objects.all()
    return HttpResponse(c_list)


from .models import course


def course(request):

    if request.method == "POST":

        Course.objects.create(
            course=request.POST.get("course"),
            duration=request.POST.get("duration"),
            fee=request.POST.get("fee"),
            trainer_name=request.POST.get("trainer_name"),
            mode_onlineoffline=request.POST.get("mode_onlineoffline"),
            start_date=request.POST.get("start_date"),
            noof_seats=request.POST.get("noof_seats"),
            course_status=request.POST.get("course_status")
        )

        return redirect("course")

    courses = Course.objects.all()

    return render(
        request,
        "myapp/course.html",
        {"courses": courses}
    )
    