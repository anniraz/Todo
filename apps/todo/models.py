from django.db import models

from apps.user.models import User


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    title=models.CharField(max_length=255, unique=True)
    description=models.TextField(blank=True,null=True)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='todo_img/',blank=True,null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        unique_together = ('user', 'title')

        