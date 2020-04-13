from django.db import models

# Create your models here.
class book(models.Model):
    OneOfNovel = 'One of Novel'
    Documentation = 'Documentation'
    Other = 'Other'
    TYPR_OF_BOOK_CHOICES = [
        (OneOfNovel, 'One of Novel'),
        (Documentation, 'Documentation'),
        (Other, 'Other'),
    ]
    title = models.CharField(max_length=160)
    author = models.CharField(max_length=100)
    datePublished = models.DateField()
    numberOfPages = models.IntegerField()
    typeOfBook = models.CharField(max_length=15, choices=TYPR_OF_BOOK_CHOICES, default=OneOfNovel)

    def __str__(self):
        return self.title