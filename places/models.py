from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField("Название", max_length=200)
    description_short = models.TextField(
        "Краткое описание",
        blank=True,
        null=True
        )
    description_long = models.TextField(
        "Полное описание",
        blank=True,
        null=True
        )
    
    lng = models.FloatField('Долгота', null=True, blank=True)
    lat = models.FloatField('Широта', null=True, blank=True)

    def __str__(self):
        return self.title
