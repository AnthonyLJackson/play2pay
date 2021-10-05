from django.contrib import admin
from .models import Book, UserProfile,Library,Transaction

# Register your models here.
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Library)

class TransactionAdmin(admin.ModelAdmin):
    # Due Date will be automatically populated on save when there is a checkout date
    readonly_fields=('due_date',)

    # Displaying the columns in the admin
    list_display = ['book_title','borrower','due_date']
admin.site.register(Transaction, TransactionAdmin)
