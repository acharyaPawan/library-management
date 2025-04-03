from django import forms
from .models import Student
from datetime import date

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_id', 'name', 'date_of_birth', 'address']
    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
    }

  def clean_student_id(self):
    student_id = self.cleaned_data.get('student_id')
    if not student_id:
      raise forms.ValidationError("Student ID is required.")
    if not student_id.isalnum():
      raise forms.ValidationError("Student ID must be alphanumeric.")
    return student_id

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if not name:
      raise forms.ValidationError("Name is required.")
    if len(name) < 3:
      raise forms.ValidationError("Name must be at least 3 characters long.")
    return name

  def clean_date_of_birth(self):
    date_of_birth = self.cleaned_data.get('date_of_birth')
    if not date_of_birth:
      raise forms.ValidationError("Date of Birth is required.")
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    if age < 10:
      raise forms.ValidationError("Student must be at least 10 years old.")
    return date_of_birth

  def clean_address(self):
    address = self.cleaned_data.get('address')
    if not address:
      raise forms.ValidationError("Address is required.")
    return address