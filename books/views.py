from django.shortcuts import render, redirect
from .models import Book
from .form import AddNewBookForm, RemoveBookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = AddNewBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'books/add_book.html', {'form': form})
    else:
        form = AddNewBookForm()
    return render(request, 'books/add_book.html', {'form': form})


def remove_book(request):
    if request.method == 'POST':
        form = RemoveBookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            try:
                book = Book.objects.get(book_id=book_id)
                book.delete()  # Remove the book from the database
                return redirect('book_list')  # Redirect to a success page
            except Book.DoesNotExist:
                form.add_error('book_id', 'Book not found')  # Add an error to the form
    else:
        form = RemoveBookForm()
    return render(request, 'books/remove_book.html', {'form': form})
