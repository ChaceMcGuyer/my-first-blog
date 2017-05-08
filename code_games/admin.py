from django.contrib import admin

#import the game from .models for this app
from .models import Game


# Register your models here.
admin.site.register(Game)
