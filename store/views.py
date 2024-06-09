from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html' ,  {'books': books})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    books = Book.objects.all()
    return render(request, 'products.html', {'books': books})

def product_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'book': book})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')


#class for detailview of books
class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'

#class for search functionality using users queries
def search(request):
    query = request.GET.get('q')
    product = Book.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'product': product})
    


