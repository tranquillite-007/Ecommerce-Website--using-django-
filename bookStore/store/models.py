from django.db import models
import os

def filepath(filename):
    return os.path.join('images/book_images/', filename)



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='filepath', blank=True)


    def get_absolute_url(self):
        return f"/books/{self.pk}/"

    def __str__(self):
        return self.title
    