from django.shortcuts import render

# Create your views here.
def student(request):
    return render(request,'student/student.html')

def my_course(request):
    return render(request,'student/my_course.html')