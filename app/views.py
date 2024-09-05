from django.shortcuts import render
from .models import student
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render (request,'about.html')
def insertData(request):
    if request.method=='post':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render (request,'index.html') 