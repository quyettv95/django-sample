from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student, SubjectRegistration
from django.template.defaultfilters import slugify
from django.urls import reverse

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

    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Sinh viên không tồn tại")
    subjectRegistrations = SubjectRegistration.objects.filter(student=student)
    slugGenerate = slugify(student.name)
    print(slugGenerate)
    data = {
        "student": student,
        "subjectRegistrations": subjectRegistrations,
    }
    print(subjectRegistrations)
    return render(request, 'students/show.html', data)

def showBySlug(request, duongDan, student_id):
    # print(slug)
    student = Student.objects.get(pk=student_id)
    subjectRegistrations = SubjectRegistration.objects.filter(student=student)
    slugGenerate = slugify(student.name)
    print(slugGenerate)
    data = {
        "student": student,
        "subjectRegistrations": subjectRegistrations,
    }
    print(subjectRegistrations)
    return render(request, 'students/show.html', data)

def getStudentByClass(request, id, name):
    print(id)
    print(name)

    return HttpResponse("Danh sách sinh viên của lớp có id " + str(id) + " có tên " + name)
    # return render(request, 'students/show.html', data)

def getStudentByYear(request, year):
    print(year)

    return HttpResponse("Danh sách sinh viên của có năm sinh" + str(year))
    # return render(request, 'students/show.html', data)

def getStudentByName(request, name):

    return HttpResponse("Danh sách sinh viên có tên " + name)
    # return render(request, 'students/show.html', data)

def welcome(request):
    # Solution 1
    # std = Student.objects.get(pk=1)
    # return redirect(std)

    # Solution 2
    return redirect(reverse('student:show', args=(10,)))


    # Solution 3
    return redirect("https://google.com")

    year = 1995
    url = reverse('student:student-in-class-by-year', args=(year,))
    name = "Quyet Quyet2"
    url = reverse('student:student-in-class-by-name', args=(name,))
    return HttpResponse(url)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip