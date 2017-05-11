from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    #field for the author
    author = models.ForeignKey('auth.User')

    #field for post title
    title = models.CharField(max_length=200)

    #field for body text
    text = models.TextField()

    #save created and published date
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #field to reference images saved in static files
    image = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
