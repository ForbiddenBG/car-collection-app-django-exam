from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(MinLengthValidator(2, message="The username must be a minimum of 2 chars"),),
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=(MinValueValidator(18),),
    )

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )