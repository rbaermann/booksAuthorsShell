from django.shortcuts import render

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello')