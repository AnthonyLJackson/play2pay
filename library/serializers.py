from rest_framework import serializers
from .models import Book, UserProfile, Library, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ "title","author","isbn",]

class UserProfileSerializer(serializers.ModelSerializer):
    # Grabs the values of the ForeignKey
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    class Meta:
        model = UserProfile
        fields = "__all__"

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title","author","isbn","checked_out",]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["pk","book_title","borrower","due_date",]
