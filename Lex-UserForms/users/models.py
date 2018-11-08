from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    language_preference = models.CharField(max_length=500)
    COMMITMENT_LEVELS = (
        ('C', 'Casual'),
        ('S', 'Serious')
    )
    AGE_RANGES = (
        ('0', 'Under 18 years'),
        ('18', '18 to 24 years'),
        ('25', '25 to 34 years'),
        ('35', '35 to 44 years'),
        ('45', '45 to 54 years'),
        ('55', '55 to 64 years'),
        ('65', 'Age 65 or older'),
    )
    age_range = models.CharField(max_length=3,choices=AGE_RANGES)
    commitment_level = models.CharField(max_length=3,choices=COMMITMENT_LEVELS)
    
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
