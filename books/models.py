from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Book(models.Model):
    image = models.ImageField(upload_to = 'book_images/', blank = True)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    price = models.CharField(max_length=15)
    year = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')])
    format = models.CharField(max_length=50, default='')
    pages = models.CharField(max_length=15, default='')
    place = models.CharField(max_length=30, default='')
    age = models.CharField(max_length=4, default="0")
    description = models.TextField(max_length=2500)
    content = models.TextField(max_length=2000, default='')

    CATEGORY_CHOICES = (
            ('NEW', 'New'),
            ('BESTSELLER', 'Bestseller'),
            ('HISTORY', 'History'),
            ('SCIENCE', 'Science'),
            ('AUDIO', 'Audio')
            )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='NEW')

    def __str__(self):
        return self.name


class Comment(models.Model):
    connect_model = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length = 100)
    text = models.TextField(max_length = 600)
    date = models.DateTimeField('Date published')

    def __str__(self):
        return self.author


class Expert(models.Model):
    image = models.ImageField(upload_to = 'expert_images/', blank = True)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name



