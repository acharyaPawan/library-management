from django.shortcuts import render
from books.models import Book
from borrow.models import BorrowedBook
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    total_books = Book.objects.count()
    borrowed_books = BorrowedBook.objects.count()
    returned_books = BorrowedBook.objects.filter(return_date__isnull=False).count()

    context = {
        'total_books': total_books,
        'borrowed_books': borrowed_books,
        'returned_books': returned_books,
    }

    return render(request, 'dashboard/dashboard.html', context)
