from django.shortcuts import render, redirect
from .models import book
from .Form import addBook


# Create your views here.

def index(request):
    books = book.objects.all()
    if books == None:
        return render(request, 'Book_Form_CRUD/index_nobook.html')
    return render(request, 'Book_Form_CRUD/index.html', {'books':books})


def add(request):
    if request.method == 'POST':
        addbook = addBook(request.POST)
        if addbook.is_valid():
            addbook.save()
            return redirect('index')

    else:
        addbook = addBook()
        return render(request, 'Book_Form_CRUD/addBook_form.html', {'add_form':addbook})

def update(request, book_id):
    book_id = int(book_id)
    try:
        book_update = book.objects.get(id = book_id)
    except book.DoesNotExist:
        return redirect('index')
    addbook = addBook(request.POST or None, instance = book_update)
    if addbook.is_valid():
       addbook.save()
       return redirect('index')
    return render(request, 'Book_Form_CRUD/addBook_form.html', {'add_form':addbook})

def delete(request, book_id):
    book_id = int(book_id)
    try:
        book_delete = book.objects.get(id = book_id)
    except book.DoesNotExist:
        return redirect('index')
    book_delete.delete()
    return redirect('index')