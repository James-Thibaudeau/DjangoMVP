
from django.shortcuts import render

def about(request):
    return render(request, "about.html", {})

def thanks(request):
    return render(request, "thankyou.html", {})

def blog(request):
    return render(request, "blog.html", {})
