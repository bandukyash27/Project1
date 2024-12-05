from django.shortcuts import render

# Create your views here.
def index(request):
    d={'name':'Yaswanth',
       'age':22
       }
    return render(request,'new.html',context=d)




