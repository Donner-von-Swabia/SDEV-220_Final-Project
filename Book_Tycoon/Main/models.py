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
        return self.user