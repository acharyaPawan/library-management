from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        Student.objects.create(student_id=student_id, name=name, date_of_birth=date_of_birth, address=address)
        return redirect('student_list')

    return render(request, 'students/add_student.html')
