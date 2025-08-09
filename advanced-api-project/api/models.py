from django.db import models
from django.utils import timezone

# Author model represents a writer who can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name


# Book model represents a single book written by an author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author,               # Links this book to an Author
        related_name='books', # Allows reverse lookup: author.books.all()
        on_delete=models.CASCADE # Deletes books if the author is deleted
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

