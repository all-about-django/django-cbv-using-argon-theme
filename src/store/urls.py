from django.urls import path

from . import views


urlpatterns = [
    path('book', views.BookListView.as_view(),
         name='book-list'),
    path('book/create', views.BookCreateView.as_view(),
         name='book-create'),

]
