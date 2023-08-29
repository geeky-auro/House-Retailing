from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello</h1>');


def about(request):
    return render(request,'pages/about.html')

def above(request):
    return render(request,'pages/index.html')