from django.contrib import admin
from .models import Book, Comment, Expert

#adm

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Expert)