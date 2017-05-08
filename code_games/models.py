from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    #create a title for use in the url
    title = models.CharField(max_length=200)

    #create a place for the text to dynamically generate the game
    embed = models.CharField(max_length=200)

    #create a place for the published date
    published_date = models.DateTimeField(blank=True, null=True,)

    #create a place for the created_date
    created_date = models.DateTimeField(default=timezone.now)

    #create a palce for static image on listing page
    image = models.CharField(max_length=200, default=None, null=True,)


    #define the string representation of the object
    def __str__(self):
        return self.title
