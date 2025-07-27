from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author'].strip()
        if not author:
            raise forms.ValidationError("Author cannot be empty.")
        return author
