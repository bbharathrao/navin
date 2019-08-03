from django.shortcuts import render

from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello, All This is the website of Mr. Naveen Kumar Reddy Chappidi. I am working in IT industry from couple of year. I am an highly qualified individual in developent of websites and web projects.")