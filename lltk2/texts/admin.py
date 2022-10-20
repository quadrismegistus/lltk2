from django.contrib import admin
from .models import Author, Work, Book, Text
# Register your models here.

admin.site.register(Author)
admin.site.register(Work)
admin.site.register(Book)
admin.site.register(Text)