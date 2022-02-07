from django.db import models

# Using an ImageField to save our images, the upload to attribute will tell these images where inside the media folder to save 
# itself

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
