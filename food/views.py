from django.shortcuts import render

# Create your views here.

def biryani(request):
    return render(request,'biryani.html')

def rasgulla(request):
    return render(request,'rasgulla.html')