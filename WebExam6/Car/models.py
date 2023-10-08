from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Car(models.Model):
    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
    )

    model = models.CharField(
        max_length=20,
        validators=(MinLengthValidator(2),),
    )

    # I should check this validation!
    year = models.IntegerField(
        validators=(
            MinValueValidator(1980, message="Year must be between 1980 and 2049"),
            MaxValueValidator(2049, message="Year must be between 1980 and 2049"),
        ),
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(MinValueValidator(1),)
    )
