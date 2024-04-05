from django.shortcuts import render

# Create your views here.

def bacarid(request):
    return render(request,'bacarid.html')

def black_white(request):
    return render(request,'black_white.html')
