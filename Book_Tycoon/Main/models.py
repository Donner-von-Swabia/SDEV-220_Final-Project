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
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=256)
    body = models.TextField(max_length= 1000)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.body


