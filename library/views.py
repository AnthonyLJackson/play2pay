#We'll be using the framework's views
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Book, UserProfile, Library, Transaction
from .serializers import BookSerializer, UserProfileSerializer,LibrarySerializer, TransactionSerializer

# BOOKLIST will create our List, Get, Post
class BookList(generics.ListCreateAPIView):
    # QUERYSET: the set of object that we'll be looking over
    queryset = Book.objects.all()
    # We are going to use the BookSerializer class we defined
    serializer_class = BookSerializer

# Creates our Update,Delete, Patch
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all().order_by('due_date')
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class LibraryList(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
class LibraryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryBookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer

    # Overrides the default queryset to apply a lookup filter
    def get_queryset(self):
        # Checks kwargs for primary key sent in by urls.py
        location_id = self.kwargs['pk']
        queryset = Book.objects.filter(location=location_id)
        # Ordered by Checked out status
        return queryset.order_by('-checked_out')
