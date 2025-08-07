from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for the Book model
# This serializer includes all fields and validates that publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    # noinspection PyMethodMayBeStatic
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields in the Book model

        # Object-level validation
        def validate(self, attrs):
            publication_year = attrs.get('publication_year')
            current_year = datetime.datetime.now().year

            if publication_year > current_year:
                raise serializers.ValidationError({
                    "publication_year": "Publication year cannot be in the future."
                })

            return attrs


# Serializer for the Author model
# Includes the author's name and a nested list of their books using BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serialization: books are serialized using BookSerializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  # Only include name and related books
