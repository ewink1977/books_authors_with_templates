from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author

def index(request):
    context = {
        "books" : Book.objects.all(),
    }
    return render(request, 'html/book.html', context)

def bookview(request, bookid):
    # Code to exclude authors already added to add list!
    thisbookauthors = []
    thisbook = Book.objects.get(id=bookid)
    for id in thisbook.Author.all():
        thisbookauthors.append(id.id)

    context = {
        "bookinfo" : Book.objects.get(id=bookid),
        "authorinfo" : Author.objects.all(),
        "excludelist" : thisbookauthors
    }
    return render(request, 'html/bookview.html', context)

def addbook(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['booktitle'], desc=request.POST['bookdesc'])
    return redirect('/')

def addanauthor(request):
    if request.method == 'POST':
        bookmodify = Book.objects.get(id=request.POST['bookid'])
        authoradd = Author.objects.get(id=request.POST['authoradd'])
        bookmodify.Author.add(authoradd)
    return redirect('/')

def authors(request):
    context = {
        "authors" : Author.objects.all(),
    }
    return render(request, 'html/author.html', context)

def authview(request, authid):
    # Code to exclude books already added from add list!
    thisauthorsbooks = []
    thisauth = Author.objects.get(id=authid)
    for id in thisauth.books.all():
        thisauthorsbooks.append(id.id)

    context = {
        "bookinfo" : Book.objects.all(),
        "authorinfo" : Author.objects.get(id=authid),
        "excludelist" : thisauthorsbooks
    }
    return render(request, 'html/authview.html', context)

def authadd(request):
    if request.method == 'POST':
        Author.objects.create(first_name=request.POST['authfirst'], last_name=request.POST['authlast'], notes=request.POST['authnotes'])
    return redirect('../authors')

def addabook(request):
    if request.method == 'POST':
        authmodify = Author.objects.get(id=request.POST['authid'])
        bookadd = Book.objects.get(id=request.POST['bookadd'])
        authmodify.books.add(bookadd)
    return redirect('../authors')