from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from .models import Book, Comment, Expert #.models!!!
import datetime


def main_window(request, anch='0'):
    books = Book.objects.all()
    content = {'books': books}
    template = loader.get_template('books/main_page.html')
    return HttpResponse(template.render(content, request))   

def show_login(request, anch='0'):
    content = {}
    template = loader.get_template('books/login.html')
    return HttpResponse(template.render(content, request))   

def show_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('registered')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})

@login_required
def registered(request):
    books = Book.objects.all()
    content = {'books': books}
    template = loader.get_template('books/main_page.html')
    return HttpResponse(template.render(content, request))

def logout_view(request):
    logout(request)  
    return redirect(reverse('main_window'))

def show_book(request, arg):
    book = Book.objects.get(id=arg)
    comments = book.comments.all()
    content = {'book': book, 'comments': comments}
    template = loader.get_template('books/book_page.html')
    return HttpResponse(template.render(content, request))   

def show_payment(request):
    content = {}
    template = loader.get_template('books/payment.html')
    return HttpResponse(template.render(content, request))   

def show_return(request):
    content = {}
    template = loader.get_template('books/return.html')
    return HttpResponse(template.render(content, request))   

def add_comment(request, arg):
    connect_model = arg
    comment = request.POST.get('main_textarea')
    author = request.user.username
    date = timezone.now()
    book = Book.objects.get(id=arg)
    comments = book.comments.all()
    book.comments.create(connect_model=connect_model, author=author, text=comment, date=date)

    content = {'book': book, 'comments': comments}
    template = loader.get_template('books/book_page.html')
    return HttpResponse(template.render(content, request))   

def show_searched(request):
    entered_text = request.POST.get('top_input')
    if entered_text == "":
        entered_text = request.POST.get('top_input_hidden')
    entered_text = entered_text.capitalize()
    searched_books = Book.objects.filter(Q(name__istartswith=entered_text))
    content = {'searched_books': searched_books}
    template = loader.get_template('books/searched.html')
    return HttpResponse(template.render(content, request)) 

def show_contacts(request):
    content = {}
    template = loader.get_template('books/contacts.html')
    return HttpResponse(template.render(content, request))   

def show_help(request):
    content = {}
    template = loader.get_template('books/help.html')
    return HttpResponse(template.render(content, request))   

def show_about(request):
    content = {}
    template = loader.get_template('books/about.html')
    return HttpResponse(template.render(content, request))   

def show_news(request):
    books = Book.objects.all()
    content = {"books": books}
    template = loader.get_template('books/new.html')
    return HttpResponse(template.render(content, request))       

def show_history(request):
    books = Book.objects.all()
    content = {"books": books}
    template = loader.get_template('books/history.html')
    return HttpResponse(template.render(content, request))

def show_bestsellers(request):
    books = Book.objects.all()
    content = {"books": books}
    template = loader.get_template('books/bestsellers.html')
    return HttpResponse(template.render(content, request))   

def show_all(request):
    books = Book.objects.all()
    content = {"books": books}
    template = loader.get_template('books/all_books.html')
    return HttpResponse(template.render(content, request))   

def show_audio(request):
    books = Book.objects.all()
    content = {"books": books}
    template = loader.get_template('books/audio.html')
    return HttpResponse(template.render(content, request))   

def show_experts(request):
    experts = Expert.objects.all()
    content = {"experts": experts}
    template = loader.get_template('books/experts.html')
    return HttpResponse(template.render(content, request))