from django.shortcuts import render
from books.models import Book
from borrow.models import BorrowedBook
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    total_books = Book.objects.count()
    borrowed_books = Book.objects.filter(status='borrowed').count()
    available_books = total_books - borrowed_books

    context = {
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
    }

    print('total_books:', total_books)
    print('available_books:', available_books)
    print('borrowed_books:', borrowed_books)
    return render(request, 'dashboard/dashboard.html', context)
