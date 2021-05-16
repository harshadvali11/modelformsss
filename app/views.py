from django.shortcuts import render

# Create your views here.
import datetime
def filter(request):
    date1=datetime.datetime.now()
    return render(request,'filter.html',context={'data':'HaI HOW aRE YOu','date1':date1,'count':1})


def usd(request):
    d={'data':'hai hello HOW r u'}
    return render(request,'userfilter.html',context=d)