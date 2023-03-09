from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publicationdate = models.DateField()
    bookdescription = models.CharField(max_length=200)
    checkout = models.BooleanField()
    checkedoutuser = models.CharField(max_length=20, default = "none")

    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    user = models.CharField(max_length=256)
    published = models.DateField()
    head = models.CharField(max_length=100)
    body = models.TextField(max_length= 1000)

    def __str__(self):
        return self.user + self.body

#Reserve model is redundant as currently reservations are handled in book's properties
class Reserve(models.Model):
    reserve_id= models.IntegerField()
    username=models.CharField(max_length=15)
    pick_up= models.DateField()
    book_id=models.IntegerField()

    def __str__(self):
        return self.reserve_id
    
