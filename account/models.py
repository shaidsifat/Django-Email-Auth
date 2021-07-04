from django.db import models

# Create your models here.
class User(models.Model):
    Bio = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=300, unique=True)
    Email = models.CharField(max_length=200,unique=True)
    Phone = models.CharField(max_length=8,unique=True)
    Password = models.CharField(max_length=12)
    class Meta:
        ordering = ['Email']

    def __str__(self):
        return self.Email