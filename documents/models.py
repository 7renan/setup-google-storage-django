from django.db import models


# Create your models here.
class Document(models.Model):
    name = models.CharField('Nome', max_length=150)
    archive = models.FileField()

    def __str__(self):
        return self.name
