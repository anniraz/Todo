from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=255, unique=True)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='todo_img/')

    def __str__(self) -> str:
        return self.title
