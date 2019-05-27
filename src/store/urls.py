from django.urls import path

from . import views


urlpatterns = [
    path('book', views.BookListView.as_view(),
         name='book-list'),
]
