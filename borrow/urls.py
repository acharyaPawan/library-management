from django.urls import path
from .views import issue_book, borrowed_books, return_book

urlpatterns = [
    path('issue/', issue_book, name='issue_book'),
    path('borrowed/', borrowed_books, name='borrowed_books'),
    path('return/<int:book_id>/', return_book, name='return_book'),
]
