from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Book


@method_decorator(login_required, name='dispatch')
class BookListView(ListView):

    model = Book
    template_name = 'book/list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'book/create.html'
    fields = ('name', 'isbn_number', )
    success_url = reverse_lazy('book-list')


@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):

    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'book'
