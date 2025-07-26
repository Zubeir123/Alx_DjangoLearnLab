from .models import Author, Book, Library, Librarian


def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"\nBooks by {author_name}:")
    for book in books:
        print(f"- {book.title}")


def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library_name} Library:")
    for book in books:
        print(f"- {book.title}")


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian of {library_name}: {librarian.name}")
    print(f"\nLibrarian of {library_name}: {librarian.name}")
