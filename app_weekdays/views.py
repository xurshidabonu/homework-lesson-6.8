from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
links = f"<ul><li><a href='weekdays/en>'hafta_kuni_en</a></li><li><a href='weekdays/rus>hafta_kuni_rus</a></li><li><a href='weekdays/uz>hafta_kuni_uz</a></li></ul>

def hafta_kuni(request):
    return HttpResponse("<h1>hafta kuni</h1>")


def hafta_kuni_en(request):
    html = "<h1>hafta_kuni_en</h1>"
    html += links
    return HttpResponse(html)


def hafta_kuni_rus(request):
   html = "<h1>hafta_kuni_rus</h1>"
   html += links
   return HttpResponse(html)


def hafta_kuni_uz(request):
    html = "<h1>hafta_kuni_uz</h1>"
    html += links
    return HttpResponse(html)