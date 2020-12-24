from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/<int:bookid>', views.bookview, name='bookview'),
    path('addbook/', views.addbook, name='addbook'),
    path('addanauthor', views.addanauthor, name='addanauthor'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:authid>', views.authview, name='authview'),
    path('authadd/', views.authadd, name='authoradd'),
    path('addabook/', views.addabook, name='addabook'),
]