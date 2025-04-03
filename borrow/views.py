from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import BorrowedBook
from books.models import Book
from students.models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

def issue_book(request):
    return render(request, 'borrow/issue_book.html')





def badrequest(request, message):
    return HttpResponseBadRequest(message)

@csrf_exempt
def check_student_htmx(request):
    student_id = request.POST.get('student_id')
    try:
        student = Student.objects.get(student_id=student_id)
        return render(request, 'borrow/htmx/student_info.html', {'student': student})
    except Student.DoesNotExist:
        return render(request, 'borrow/htmx/student_info.html', {'student': False})


@csrf_exempt
def get_available_books(request):
    # student_id = request.GET.get('student_id')
    # if student_id:
    #     books = Book.objects.filter(status='available').exclude(borrowedbook__student_id=student_id)
    # else:
    print("inside get_available_books")
    
    books = Book.objects.filter(status='available')
    print("books", books)
    return render(request, 'borrow/htmx/available_books_list.html', {'books': books})

@csrf_exempt
def issue_book_htmx(request, book_id):
    # book_id = request.POST.get('book_id')
    student_id = request.POST.get('student_id')
    print("book_id",book_id, "student_id",student_id)
    try:
        book = Book.objects.get(id=book_id)
        student = Student.objects.get(student_id=student_id)
        if book.status == 'available':
            BorrowedBook.objects.create(book=book, student=student)
            book.status = 'borrowed'
            book.save()
            return render(request, 'borrow/htmx/issue_book_operation.html', {'success': 'Book issued successfully'})
        else:
            return render(request, 'borrow/htmx/issue_book_operation.html', {'error': 'Book is not available'})
    except (Book.DoesNotExist, Student.DoesNotExist):
        return render(request, 'borrow/htmx/issue_book_operation.html', {'error': 'Invalid book or student'})
    
@csrf_exempt
def issue_book_htmx2(request):
    book_id = request.POST.get('book_id')
    student_id = request.POST.get('student_id')
    print("book_id",book_id, "student_id",student_id)
    if (not book_id):
        return render(request, 'borrow/htmx/issue_book_operation.html', {'error': 'Book ID is required'})
    elif (not student_id):
        return render(request, 'borrow/htmx/issue_book_operation.html', {'error': 'Student ID is missing.'})
    try:
        book = Book.objects.get(book_id=book_id)
        student = Student.objects.get(student_id=student_id)
        print("book", book, "student", student)
        if book.status == 'available':
            BorrowedBook.objects.create(book=book, student=student)
            book.status = 'borrowed'
            book.save()
            return render(request, 'borrow/htmx/issue_book_operation.html', {'success': 'Book issued successfully'})
        else:
            return render(request, 'borrow/htmx/issue_book_operation.html', {'error': 'Book is not available'})
    except (Book.DoesNotExist, Student.DoesNotExist):
        return render(request, 'borrow/htmx/issue_book_operation.html', {'error': 'Invalid book or student'})

@csrf_exempt
def get_issued_books(request):
    print("inside get_issued_books")
    student_id = request.GET.get('student_id')
    print("student_id", student_id)
    if student_id:
        borrowed_books = BorrowedBook.objects.filter(return_date__gt=now(), student__student_id=student_id).order_by('-borrowed_date')
    else:
        borrowed_books = BorrowedBook.objects.all().filter(return_date__gt = now()).order_by('-borrowed_date')
    print("here",borrowed_books)
    return render(request, 'borrow/htmx/issued_books_list.html', {'borrowed_books': borrowed_books, 'student_id': student_id})

@csrf_exempt
def get_returned_books(request):
    student_id = request.GET.get('student_id')
    if not student_id:
        returned_books = BorrowedBook.objects.filter(return_date__lt=now()).order_by('-return_date')
        # return render(request, 'borrow/htmx/handle_error.html', {'error': 'Student ID is required'})
    else:
        returned_books = BorrowedBook.objects.filter(student__student_id=student_id, return_date__lt=now()).order_by('-return_date')
    return render(request, 'borrow/htmx/returned_books_list.html', {'returned_books': returned_books})



@csrf_exempt
def return_book(request):
    borrowed_book_id = request.POST.get('borrowed_book_id')
    print("borrowed_book_id", borrowed_book_id)
    student_id = request.POST.get('student_id')
    # if not borrowed_book_id:
    #     return render(request, 'borrow/htmx/return_book_operation.html', {'error': 'Borrowed Book ID is required'})
    if not student_id:
        return render(request, 'borrow/htmx/return_book_operation.html', {'error': 'Student ID is missing.'})
    try:
        borrowed_book = BorrowedBook.objects.get(book__book_id = borrowed_book_id, student__student_id = student_id, return_date__gt=now())
        print("borrowed_book", borrowed_book)
        
        borrowed_book.return_date = now()
        borrowed_book.book.status = 'available'
        borrowed_book.book.save()
        borrowed_book.save()
        return render(request, 'borrow/htmx/return_book_operation.html', {'success': 'Book returned successfully'})
    except BorrowedBook.DoesNotExist:
        return render(request, 'borrow/htmx/return_book_operation.html', {'error': 'Invalid borrowed book'})
