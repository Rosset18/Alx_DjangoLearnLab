from django.db import models
from datetime import datetime

# Author model stores the name of the author.
# An Author can have multiple books (One-to-Many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores book details and links to an Author via ForeignKey.
# This allows retrieving all books written by a given Author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

