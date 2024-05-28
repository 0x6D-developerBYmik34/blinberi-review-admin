from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Brand(models.Model):
    # title может быть unique and primary key
    title = models.CharField(
        "brand unique name", 
        primary_key=True,
    ) #pot key
    desctiption = models.TextField()
    active_on_rank = models.BooleanField(default=True)
    # logo

    def __str__(self):
        return f"{self.title}"


class City(models.Model): #все города России
    tel_city_code = models.IntegerField(
        "Телефонный код города",
        primary_key=True,
    )
    name = models.CharField()
    # region_code - на будущее

    def __str__(self):
        return f"{self.name} ({self.tel_city_code})"


class Location(models.Model): # другой pk 
    title = models.CharField()  # pot key
    addres = models.TextField()
    active_on_rank = models.BooleanField(default=True)
    point = models.JSONField()  # {lat: float, lon: float} по хорошему это pk
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True
    )
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.SET_NULL,
        null=True
    )


class Review(models.Model):
    resorce = models.CharField() 
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    ) 
    review = models.TextField()
    date =  models.DateField()
    location = models.ForeignKey(
        Location, 
        on_delete=models.SET_NULL, 
        null=True
    )
