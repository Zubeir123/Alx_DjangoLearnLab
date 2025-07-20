from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('library_detail/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('list_books/', list_books, name='book_list'),
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', member_view, name='member_dashboard'),
]

