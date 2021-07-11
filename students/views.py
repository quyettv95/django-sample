from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    students = Student.objects.all()
    data = {
        'students': students,
        'genderMeta': {
            1: "Nam",
            2: "Nữ",
        }
    }

    return render(request, 'students/index.html', data)

def show(request, student_id):
    student = Student.objects.get(pk=student_id)
    data = {
        "student": student
    }
    return render(request, 'students/show.html', data)

def welcome(request):
    return HttpResponse("Đây là trang welcome")



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip