from django.shortcuts import render

# Create your views here.
def home(request):
    d={'name':'farhan','age':23}
    return render(request,'home.html',d)