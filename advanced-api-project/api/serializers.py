from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


# Serializes Book model fields
# Includes custom validation for publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future ({current_year})."
            )
        return value


# Serializes Author model and nests the BookSerializer
# books field is populated dynamically from the related_name in the Book model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

