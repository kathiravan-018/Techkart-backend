from django.db import models

# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Profile(models.Model):

   
    username = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(
    max_length=10,
    choices=[
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
)
    phone = models.CharField(max_length = 15)
    address = models.TextField()