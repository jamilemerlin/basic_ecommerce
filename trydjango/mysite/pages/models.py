from django.db import models


# Create your models here.
class Banner(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=120)
    image_alt = models.TextField(blank=True, null=True)
    link = models.URLField(null=True)

    def __str__(self):
        return self.title

class Services(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=120)
    image_alt = models.TextField(blank=True, null=True)
    link = models.URLField(null=True)


class Video(models.Model):
    title = models.CharField(max_length=120)
    code = models.TextField(blank=True, null=True)
