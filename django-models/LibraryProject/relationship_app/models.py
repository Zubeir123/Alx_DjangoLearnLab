from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_add_book', 'Can add a book'),
            ('can_change_book', 'Can change a book'),
            ('can_delete_book', 'Can delete a book'),
        ]

    def __str(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('librarian', 'Librarian'),
        ('member', 'Member'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"