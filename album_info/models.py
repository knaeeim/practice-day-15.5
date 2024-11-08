from django.db import models
from musician_info.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    RATING_CHOICES = [
        (1, '1-Poor'),
        (2, '2-Not Good'),
        (3, '3-Good'),
        (4, '4-Very Good'),
        (5, '5-Excellent'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self) -> str:
        return f"{self.album_name}"
