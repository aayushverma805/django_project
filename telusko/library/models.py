from django.db import models

# Create your models here.
from django.db import models 


class Author(models.Model):
    Author_name = models.CharField(max_length=200)
    Book_id = models.IntegerField


class Book(models.Model):
    Book_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    Book_title = models.IntegerField

#class book_view(models.Model):
#    Book_id  models.IntegerField
#    Book_title models.CharField(max_length=200)
#    Author_Name models.CharField(max_length=200)
class Meta:
        managed = False
        db_table = 'book_view'