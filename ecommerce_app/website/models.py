from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    publisher = models.CharField(max_length=255)
    image_url_l = models.URLField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    genres = models.CharField(max_length=255, default='')
    rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pages = models.TextField(blank=True, null=True)
    number_of_books = models.IntegerField(default=0)

    def __str__(self):
        return self.title

