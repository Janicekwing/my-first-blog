from django.contrib import admin
from .models import Post

admin.site.register(Post) # to make the model visible on the admin page, you have to register the model
