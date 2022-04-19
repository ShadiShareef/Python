from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('author', views.author),
    path('addbook',views.addbook),
    path('addauthor',views.addauthor),
    path('book/<int:bookid>',views.bookdata),
    path('book/addAuthorToThisBook',views.addAuthorToThisBook),
    path('author/<int:authorid>',views.authordata),
    path('author/addBookToThisAuthor',views.addBookToThisAuthor)
]