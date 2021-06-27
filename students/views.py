from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ip = get_client_ip(request)
    print(ip)
    return HttpResponse("Chào bạn, bạn đang ở trang danh sách sinh viên")

def welcome(request):
    return HttpResponse("Đây là trang welcome")



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip