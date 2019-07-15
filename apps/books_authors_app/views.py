from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {}
    context['books'] = Book.objects.all()
    return render(request, 'books_authors_app/index.html', context)

def addbook(request):
    if request.method == 'POST':
        newBook = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
        )
        newBook.save()
    return redirect('/')

def bookDesc(request, bookID):
    context = {}
    context['books'] = Book.objects.get(id=bookID)
    context['book_authors'] = Book.objects.get(id=bookID).authors.all()
    context['all_authors'] = Author.objects.all()
    return render(request, 'books_authors_app/bookDesc.html', context)

def bookAuthor(request, bookID):
    if request.method == 'POST':
        author = Author.objects.get(id=request.POST['author'])
        books = Book.objects.get(id=bookID)
        books.authors.add(author)
    return redirect(f'/{bookID}/desc')

def destroy(request, bookID):
    delBook = Book.objects.get(id=bookID)
    delBook.delete()
    return redirect('/')



def author(request):
    context = {}
    context['authors'] = Author.objects.all()
    return render(request, 'books_authors_app/authors.html', context)

def addauthor(request):
    if request.method == 'POST':
        newAuthor = Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes'],
        )
        newAuthor.save()
    return redirect('/author')

def authorDesc(request, authorID):
    context = {}
    context['authors'] = Author.objects.get(id=authorID)
    context['author_books'] = Author.objects.get(id=authorID).books.all()
    context['all_books'] = Book.objects.all()
    return render(request, 'books_authors_app/authorDesc.html', context)

def authorBook(request, authorID):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['books'])
        authors = Author.objects.get(id=authorID)
        authors.books.add(book)
    return redirect(f'/author/{authorID}/desc')

def destroyAuthor(request, authorID):
    delAuthor = Author.objects.get(id=authorID)
    delAuthor.delete()
    return redirect('/author')
