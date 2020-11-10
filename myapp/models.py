from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=256)
    alias = models.CharField(max_length=250)

    def __str__(self):
        return self.name
        # return self.alias
        # return self.name + " " + self.alias
