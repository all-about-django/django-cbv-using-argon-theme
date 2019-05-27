from django.urls import path

from . import views


urlpatterns = [
    path('book', views.BookListView.as_view(),
         name='book-list'),
    path('book/create', views.BookCreateView.as_view(),
         name='book-create'),
    path('book/<int:pk>', views.BookDetailView.as_view(),
         name='book-detail'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(),
         name='book-update'),


]
