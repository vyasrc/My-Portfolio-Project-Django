from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]