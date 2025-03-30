from django.db import models

# Create your models here.
class BorrowedBook(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE,)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.name} borrowed by {self.student.name}"
