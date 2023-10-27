from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField()

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)