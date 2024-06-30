from django.shortcuts import render
from models import *

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def books(request):
    books = Books.objects.all()
    context = {'all_books': books}
    return render(request, 'books.html', context=context)