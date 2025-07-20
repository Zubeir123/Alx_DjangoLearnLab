from .models import Book
from .models import Library
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from .forms import RegisterForm

def list_books(request):
      books = Book.objects.all()
      context = {'book_list': books}
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['library_books'] = library.books.all()
        context['librarian'] = getattr(library, 'librarian', None)
        return context


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('book_list')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'relationship_app/register.html', {'form': form})