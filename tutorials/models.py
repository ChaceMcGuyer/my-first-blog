from django.db import models
from django.utils import timezone
# Create your models here.
class Tutorials(models.Model):
    #change admin name
    verbose_name_plural = "Tutorials"
    #field for author
    author = models.ForeignKey('auth.User')

    #field to specify programming language
    language = models.CharField(max_length=200)

    #field for tutorial title
    title = models.CharField(max_length=200)

    #first section of page text
    text_one = models.TextField()

    #first section of code will be formatted with bootstrap `code` style
    code_one = models.TextField()

    #second section of page text after the code
    text_two = models.TextField()

    #second section of code if more is needed
    code_two = models.TextField()

    #image field to reference image name in static files
    image = models.CharField(max_length=200)

    #fields for created and published dates
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
