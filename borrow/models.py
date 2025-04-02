from django.db import models
from datetime import timedelta
from django.utils.timezone import get_current_timezone
from datetime import datetime

# Create your models here.
class BorrowedBook(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE,)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    def default_return_date():
        now = datetime.now(get_current_timezone())
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
        return end_of_day + timedelta(days=14)

    return_date = models.DateTimeField(default=default_return_date, null=True, blank=True)

    def __str__(self):
        return f"{self.book.name} borrowed by {self.student.name}"
