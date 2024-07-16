from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

    def __str__(self):
        return self.name
