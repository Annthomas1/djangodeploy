from django.shortcuts import render
from django.http import HttpResponse


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('aromac', 'networkzsystems.com')
    return response


def getcookie(request):
    tutorial = request.COOKIES['aromac']
    return HttpResponse("aroma: " + tutorial);