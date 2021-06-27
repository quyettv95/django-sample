from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Đây là trang chủ")

def contact(request):
    return HttpResponse("Đây là trang liên lạc")

