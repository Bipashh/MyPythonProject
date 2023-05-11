from django.shortcuts import render
# Create your views here.
def demo(request):
    context={
        "class_name":"Django class",
        "date" : "2023-05-11"
    }
    return render (request,'demo.html',context)