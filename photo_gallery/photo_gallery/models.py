from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.
class photo_metadata(models.Model):
    description = models.TextField(blank=True)
    category = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img")
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(800, 600)],format='JPEG', options={'quality' : 60})

    def __str__(self):
        return self.id
