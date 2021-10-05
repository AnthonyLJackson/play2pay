from django.urls import path
from . import views

#Creats our endpoints
urlpatterns = [
    path("books/", views.BookList.as_view()),
    path("books/<int:pk>", views.BookDetail.as_view()),

    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view()),

    path("library/", views.LibraryList.as_view()),
    path("library/<int:pk>/books", views.LibraryBookList.as_view()),

    path("transactions/", views.TransactionList.as_view()),
    path("transactions/<int:pk>", views.TransactionDetail.as_view()),

]
