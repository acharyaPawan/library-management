from django.urls import path
from .views import student_list, add_student, delete_student

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student')
]
