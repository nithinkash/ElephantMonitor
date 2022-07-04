from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DataPosterTemplate(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_description = models.CharField(max_length=255, blank=False)
    elephant_description = models.CharField(max_length=255, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='posts/photos', blank=False)

