from django.urls import path
from .views import issue_book, check_student_htmx, get_available_books, issue_book_htmx, get_issued_books, return_book, get_returned_books, issue_book_htmx2

urlpatterns = [
    path('issue/', issue_book, name='issue_book'),
    path('check-student/', check_student_htmx, name='check_student'),
    path('available-books/', get_available_books, name='available_books'),
    path('issued-books/', get_issued_books, name='issued_books'),
    path("issue-book-htmx/<book_id>", issue_book_htmx, name="issue_book_htmx"),
    path("issue-book-htmx2/", issue_book_htmx2, name="issue_book_htmx2"),
    path('returned-books/', get_returned_books, name='returned_books'),
    path('return-book', return_book, name='return_book'),
]
