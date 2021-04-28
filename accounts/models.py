from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    is_expert = models.BooleanField(default=False)
    balance = models.PositiveIntegerField(default=0)
    all_time_balance = models.PositiveIntegerField(default=0)
