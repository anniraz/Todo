from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.username