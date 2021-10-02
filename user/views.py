from django.shortcuts import render , HttpResponse
from django.views import View
# Create your views here.


def show_new(View):
    return HttpResponse("<h1>CHECK 123</h1>")

def show_num(View, num):
    return HttpResponse("<h1>Đây là Số nhập vào : " + str(num) + "</h1")

def show_str(View, val):
    return HttpResponse("<h2>Đây là Str nhập vào :</h2>"+ val)

def show_cq(View, btcq):
    return HttpResponse("<h3>Show là biểu thức chính quý : "+ btcq +"</h3>")