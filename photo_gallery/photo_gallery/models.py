from django.db import models
from django.db.models.signals import post_delete
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


# Create your models here.
class photo_metadata(models.Model):
    description = models.TextField(blank=True)
    category = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img")
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(1920, 1080)], format='JPEG',
                               options={'quality': 60})

    def __str__(self):
        return self.id

    @property
    def category_format(self):
        dic = {"landscape": "Landscapes", "portrait": "Portraits", "innovation": "Innovations"}
        return dic.get(self.category, "-")