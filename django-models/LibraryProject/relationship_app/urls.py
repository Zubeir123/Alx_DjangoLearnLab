from django.urls import path
from . import views

urlpatterns = [
    path('library_detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('list_books/', views.book_list, name='book_list'),
]