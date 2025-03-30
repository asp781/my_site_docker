from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
