from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def book_list(request):
      books = Book.objects.all()
      context = {'book_list': books}
      return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'library_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    library = self.get_object()
    context['library details'] = library.all()











# from django.views.generic import DetailView
# from .models import Book
#
# class BookDetailView(DetailView):
#   """A class-based view for displaying details of a specific book."""
#   model = Book
#   template_name = 'books/book_detail.html'
#
#   def get_context_data(self, **kwargs):
#     """Injects additional context data specific to the book."""
#     context = super().get_context_data(**kwargs)  # Get default context data
#     book = self.get_object()  # Retrieve the current book instance
#     context['average_rating'] = book.get_average_rating()
