from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ---------------------------------------------------
# LIST VIEW — Retrieve all books
# ---------------------------------------------------
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ---------------------------------------------------
# DETAIL VIEW — Retrieve one book by ID
# ---------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book by its ID.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ---------------------------------------------------
# CREATE VIEW — Add a new book
# ---------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create new books.
    Validates publication_year before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------------------------------
# UPDATE VIEW — Modify an existing book
# ---------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update existing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------------------------------
# DELETE VIEW — Remove a book
# ---------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

