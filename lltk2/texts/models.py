MAX_CHAR_FIELD = 1000
from django.db import models

class Author(models.Model):
    # attrs
    name = models.CharField(max_length=MAX_CHAR_FIELD)
    dob = models.IntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                models.functions.Lower('name'),
                'dob',
                name='name_dob_unique'
            )
        ]

    def __repr__(self):
        return f'<Author #{self.id}: {self.name}>'
    
    def get_author(self):
        return self

class Work(models.Model):
    # rels
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    # attrs
    title = models.CharField(max_length=MAX_CHAR_FIELD, blank=True)

    def __repr__(self):
        return f'<Work #{self.id}: {self.title}, by {repr(self.author)}>'

    def get_author(self): return self.author

class Book(models.Model):
    # rels
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=True, null=True)
    # attrs
    title = models.CharField(max_length=MAX_CHAR_FIELD, blank=True)
    year = models.IntegerField(blank=True, null=True)

    def __repr__(self):
        return f'<Book #{self.id}: {repr(self.title)}, in {repr(self.work)}>'

    def get_author(self):
        if self.author: return self.author
        if self.work and self.work.author: return self.work.author

class Text(models.Model):
    # rels
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

    # attrs
    title = models.CharField(max_length=MAX_CHAR_FIELD, blank=True)
    txt = models.TextField()
    
    def __repr__(self):
        tistr=repr(' '.join(self.txt[:25].strip().split())+" ...")
        return f'''<Text #{self.id}: {tistr} ({len(self.txt)} chars), in {repr(self.book)}>'''

    
    def get_author(self):
        if self.author: return self.author
        if self.book and self.book.author: return self.book.author
        if self.work and self.work.author: return self.work.author
        if self.book and self.book.work and self.book.work.author: return self.book.work.author
