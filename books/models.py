from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]

    name = models.CharField(max_length=255)
    book_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Custom logic (if any)
        super().save(*args, **kwargs)  # Ensure the instance is saved
