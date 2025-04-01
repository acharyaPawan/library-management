from django import forms
from .models import Book
class AddNewBookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['name', 'book_id', 'status']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book name'}),
      'book_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book ID'}),
      'status': forms.Select(attrs={'class': 'form-control'}),
    }

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if not name:
      raise forms.ValidationError("This field is required.")
    if len(name) < 3:
      raise forms.ValidationError("Book name must be at least 3 characters long.")
    return name

  def clean_book_id(self):
    book_id = self.cleaned_data.get('book_id')
    if not book_id:
      raise forms.ValidationError("This field is required.")
    if not book_id.isalnum():
      raise forms.ValidationError("Book ID must be alphanumeric.")
    return book_id
  
  
class RemoveBookForm(forms.Form):
  book_id = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book ID to remove'})
  )
  def clean_book_id(self):
    book_id = self.cleaned_data.get('book_id')
    if not book_id:
      raise forms.ValidationError("This field is required.")
    if not book_id.isalnum():
      raise forms.ValidationError("Book ID must be alphanumeric.")
    return book_id