from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    #LANGUAGE_CHOICES = (
    #    ('ENG', 'English'),
    #   ('SPA', 'Spanish'),
    #    ('FRE', 'French'),
    #    ('GER', 'German'),
    #)
    #language_preference = MultiSelectField(max_length=3, choices=LANGUAGE_CHOICES, default='English')
    language_preference = models.CharField(max_length=500)
    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
