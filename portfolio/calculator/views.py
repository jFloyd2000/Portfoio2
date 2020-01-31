from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'calculator/index.html', {})

def add(request, a, b):
    rtnStr = "" + str(a) + " + " + str(b)
    answer = a + b;
    return render(request, 'calculator/Answer.html', {'ansStr':rtnStr, 'answer':answer})

def subtract(request, a, b):
    rtnStr = "" + str(a) + " - " + str(b)
    answer = a - b;
    return render(request, 'calculator/Answer.html', {'ansStr':rtnStr, 'answer':answer})

def multiply(request, a, b):
    rtnStr = "" + str(a) + " * " + str(b)
    answer = a * b;
    return render(request, 'calculator/Answer.html', {'ansStr':rtnStr, 'answer':answer})

def divide(request, a, b):
    rtnStr = "" + str(a) + " / " + str(b)
    answer = a / b;
    return render(request, 'calculator/Answer.html', {'ansStr':rtnStr, 'answer':answer})
