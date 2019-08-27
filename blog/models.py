from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): # defining an object named 'Post', models.Model means Post is a Django Model, so it should be saved in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # foreignkey is a link to another model
    title = models.CharField(max_length=200) # charfield is how you define text with limited characters
    text = models.TextField() # textfield is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now) # date and time
    published_date= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # double underscore = dunder
        return self.title 
