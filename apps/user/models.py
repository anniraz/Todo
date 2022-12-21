from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username=models.CharField(max_length=255, unique=True)
    email=models.EmailField()
    phone_number=PhoneNumberField()
    created_at=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.username