from django.db import models

# Create your models here.
class photo_metadata(models.Model):
    id = models.IntegerField(),
    description = models.TextField(),
    category = models.TextField(),
    published_at = models.DateTimeField()

    def __str__(self):
        return self.id
