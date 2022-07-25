from django.db import models
from django.core.validators import MinLengthValidator


class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField(max_length=1000)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.feedback} - {self.rating}'
