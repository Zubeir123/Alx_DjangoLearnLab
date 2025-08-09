from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters

# List all books
class BookListView(generics.ListAPIView):
    """
    Returns a list of all Book instances.

    Supports:
    - Filtering: ?title=BookTitle or ?author__name=AuthorName or ?publication_year=2024
    - Searching: ?search=keyword
    - Ordering: ?ordering=title or ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']  # Allows search like ?search=title


# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single Book instance by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Must be logged in


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates a Book instance.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book instance.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

