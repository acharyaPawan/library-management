from django.shortcuts import render, redirect

from .models import Student
from borrow.models import BorrowedBook
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

@csrf_exempt
def student_list(request):
    students = Student.objects.all()
    print(students);
    return render(request, 'students/students.html', {'students': students})

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        Student.objects.create(student_id=student_id, name=name, date_of_birth=date_of_birth, address=address)
        print(f"Student {name} added successfully.")
        return redirect('student_list')
    return render(request, 'students/add_student.html')

@csrf_exempt
def delete_student(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
        
        # Make borrowed books available
        borrowed_books = BorrowedBook.objects.filter(student=student, return_date__gt= now().date())
        for book in borrowed_books:
            book.status = 'available'  # Assuming 'available' is the status for available books
            book.save()
        
        student.delete()
        print(f"Student {student.name} and their borrowed books are updated successfully.")
    except Student.DoesNotExist:
        print(f"Student with ID {student_id} does not exist.")
    return redirect('student_list')
