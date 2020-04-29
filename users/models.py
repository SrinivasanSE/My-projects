from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    CHOICES = (
        ('STUDENT', 'STUDENT'),
        ('EMPLOYEE', 'EMPLOYEE'),
        ('ENTREPRENEUR', 'ENTREPRENEUR'),
        ('OTHERS', 'OTHERS'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    Occupation = models.CharField(choices=CHOICES, null=True, blank=True, max_length=15)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'
