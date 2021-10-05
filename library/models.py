from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class UserProfile(models.Model):
    # Associate this model with default Django User Model using OneToOneField
    user         = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio          = models.TextField(default="none")

    # Prints a more readable name in admin interface
    def __str__(self):
        return str(self.user.first_name+" "+self.user.last_name)

class Library(models.Model):
    name        = models.CharField(max_length=30)

    # Corrects Django plural form of Library in the admin
    class Meta:
        verbose_name_plural = "Libraries"

    def __str__(self):
        return self.name

class Book(models.Model):
    title       = models.CharField(max_length=255)
    author      = models.CharField(max_length=100)
    description = models.TextField(default="none")
    isbn        = models.CharField(max_length=13, blank=True, null=True)
    checked_out = models.BooleanField(default=True)
    pub_date    = models.DateField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits= 5, blank=True, null=True)
    location    = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    book_title  = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower    = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date        = models.DateField(blank=True, null=True)
    due_date    = models.DateField(blank=True, null=True, help_text="Auto-magically calculated to 15 days")

    def save(self, *args, **kwargs):
        # Checks if model instance is being created or updated
        if self.id:
            self.due_date = self.date + timedelta(days=15)

        # call and return default save method after custom rule
        return super(Transaction, self).save(*args, **kwargs)
