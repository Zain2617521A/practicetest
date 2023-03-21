from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateField(null=True)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title