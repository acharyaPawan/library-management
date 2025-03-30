from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name
