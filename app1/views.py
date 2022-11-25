from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':60}
    return render(request,'a1_first.html',d)

def a1_first(request):
    d={'g':30,'s':100}
    return render(request,'a1_first.html',d)

def a1_second(request):
    d={'a':200,'b':798,'c':234}
    return render(request,'a1_second.html',d)