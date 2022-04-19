from django.shortcuts import render, HttpResponse,redirect
from app import models

from app.models import Book,Author

def index(request):
    context={
        'allBook': Book.objects.all()  
    }

    return render(request,"addbook.html",context)

def author(request):
    context={
        'allAuthor': Author.objects.all()  
    }
    return render(request,"addauthor.html",context)

def addbook(request):

    bookTitle=request.POST['title']
    bookDescription=request.POST['description']
    Book.objects.create(title=bookTitle,description=bookDescription)
    return redirect('/')

def addauthor(request):
    autherFirstName=request.POST['firstName']
    autherLastName=request.POST['lastName']
    authorNotes=request.POST['notes']
    Author.objects.create(firstName=autherFirstName,lastName=autherLastName,notes=authorNotes)
    return redirect('/author')

def bookdata(request,bookid):
    context={    
        'bookdata':models.Book.objects.get(id=int(bookid)),
        'authordata':Author.objects.all()
        }
    return render(request,"viewBook.html",context)

def addAuthorToThisBook(request):
    idbook=request.POST['book_id']
    idauthor=request.POST['selectAuthor']

    this_book=Book.objects.get(id=int(idbook))
    this_author=Author.objects.get(id=int(idauthor))

    this_book.Authors.add(this_author)
    
    return render(request,"viewBook.html")

def authordata(request,authorid):
    context={    
        'authordata':models.Author.objects.get(id=int(authorid)),
        'bookdata':Book.objects.all()
        }
    return render(request,"viewAuthor.html",context)

def addBookToThisAuthor(request):

    idauthor=request.POST['author_id']
    idbook=request.POST['selectBook']

    this_book=Book.objects.get(id=int(idbook))
    this_author=Author.objects.get(id=int(idauthor))

    this_book.Authors.add(this_author)
    
    return render(request,"viewAuthor.html")