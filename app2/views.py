from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':29,'b':34,'c':56}
    return render(request,'a2_first.html',d)


def a2_second(request):
    d={'name':'GOUSIYA'}
    return render(request,'a2_second.html',d)