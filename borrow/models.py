from django.db import models
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.
class BorrowedBook(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE,)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=lambda: now().date() + timedelta(days=14), null=True, blank=True)

    def __str__(self):
        return f"{self.book.name} borrowed by {self.student.name}"
