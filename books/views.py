from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    print("I am here")
    return render(request, 'books/books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        book_id = request.POST.get('book_id')
        Book.objects.create(name=name, book_id=book_id)
        return redirect('book_list')

    return render(request, 'books/add_book.html')
