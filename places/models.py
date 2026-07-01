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

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(
        'Картинки',
        upload_to='places_images/',
        null=True,
        blank=True,
        )
    order = models.PositiveIntegerField('Порядковый номер', default=0)
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"{self.order} {self.place.title}"
    