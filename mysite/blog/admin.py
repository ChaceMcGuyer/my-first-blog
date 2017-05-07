from django.contrib import admin
from .models import Post

# Register your models here.
# This makes the model visibile on the admin page
admin.site.register(Post)
