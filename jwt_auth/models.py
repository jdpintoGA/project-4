from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    BUSINESS = 'BA'
    INDIVIDUAL = 'IN'
    USER_TYPE_CHOICES = [
        (BUSINESS, 'Business'),
        (INDIVIDUAL, 'Individual'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=INDIVIDUAL,
    )

    def __str__(self):
        return self.username
