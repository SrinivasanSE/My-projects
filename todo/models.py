from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('todo:detail',kwargs={'pk':self.pk})