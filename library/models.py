from django.db import models


class Publisher(models.Model):
    pub = models.CharField(max_length=250)

    def __str__(self):
        return self.pub


class Author(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    def __str__(self):
       return self.name + '  ' + self.surname


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=250)
    page_amount = models.CharField(max_length=250)
    lendby = models.ForeignKey('auth.User', blank=True, null=True)
    lendperiod = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title