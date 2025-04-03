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
        
        try:
            if Student.objects.filter(student_id=student_id).exists():
                error_message = f"Student with ID {student_id} already exists."
                print(error_message)
                return render(request, 'students/add_student.html', {'error': error_message})
            
            Student.objects.create(student_id=student_id, name=name, date_of_birth=date_of_birth, address=address)
            print(f"Student {name} added successfully.")
        except Exception as e:
            print(f"Error adding student: {e}")
            return render(request, 'students/add_student.html', {'error': "An Unexpected error occurred."})
        return redirect('student_list')
    return render(request, 'students/add_student.html')

@csrf_exempt
def delete_student(request):
    student_id = request.GET.get('student_id')
    print("student_id", student_id)
    if not student_id:
        raise ValueError("Student ID is required")
    try:
        student = Student.objects.get(student_id=student_id)
        
        # Make borrowed books available
        borrowed_books = BorrowedBook.objects.filter(student=student, return_date__gt = now())
        print(borrowed_books)
        for book in borrowed_books:
            book.book.status = 'available'  # Assuming 'available' is the status for available books
            book.book.save()
        
        student.delete()
        print(f"Student {student.name} and their borrowed books are updated successfully.")
    except Student.DoesNotExist:
        print(f"Student with ID {student_id} does not exist.")
    return redirect('student_list')
