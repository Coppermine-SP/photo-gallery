from django.db import models

# Create your models here.
class photo_metadata(models.Model):
    description = models.TextField(blank=True)
    category = models.TextField()
    published_at = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.id
