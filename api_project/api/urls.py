from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    # /token/ endpoint allows users to obtain an auth token via POST (username & password)
    path('token/', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
