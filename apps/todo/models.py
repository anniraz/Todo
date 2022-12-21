from django.db import models

from apps.user.models import User


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255, unique=True)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='todo_img/')

    def __str__(self) -> str:
        return self.title
