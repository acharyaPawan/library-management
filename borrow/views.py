from django.shortcuts import render, redirect
from .models import BorrowedBook
from books.models import Book
from students.models import Student

def issue_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        student_id = request.POST.get('student_id')

        book = Book.objects.get(id=book_id)
        student = Student.objects.get(id=student_id)

        if book.status == 'available':
            BorrowedBook.objects.create(book=book, student=student)
            book.status = 'borrowed'
            book.save()
        return redirect('borrowed_books')

    books = Book.objects.filter(status='available')
    students = Student.objects.all()
    return render(request, 'borrow/issue_book.html', {'books': books, 'students': students})

def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'borrow/borrowed_books.html', {'borrowed_books': borrowed_books})

def return_book(request, book_id):
    borrowed_book = BorrowedBook.objects.get(id=book_id)
    borrowed_book.return_date = datetime.date.today()
    borrowed_book.book.status = 'available'
    borrowed_book.book.save()
    borrowed_book.save()
    return redirect('borrowed_books')
