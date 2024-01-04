from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='')
    twitter = models.CharField(max_length=50, default='')
    facebook = models.CharField(max_length=50, default='')
    instagram = models.CharField(max_length=50, default='')
    linkedin = models.CharField(max_length=50, default='')
    github = models.CharField(max_length=50, default='')
    birth_date = models.DateField(default='1901-01-01')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        # img = Image.open(self.image.path)

        # if img.height > 400 or img.width > 400:
        #     output_size = (400, 400)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)