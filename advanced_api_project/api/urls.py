from django.urls import path
from .views import BookListCreateAPIView, AuthorListAPIView

urlpatterns = [
    path('api/books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('api/authors/', AuthorListAPIView.as_view(), name='author-list'),
]
